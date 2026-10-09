#!/usr/bin/env python3
"""Educational small-file envelope for synthetic OASIS exercises only.

Format: magic/version (8 bytes), random GCM nonce (12 bytes), ciphertext+tag.
Context is authenticated as AAD, not stored in the envelope. No streaming,
production key lifecycle, sender signatures, or rollback protection is provided.
"""
import argparse
import hashlib
import os
from pathlib import Path

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MAGIC = b'OASISG01'
LIMIT = 1024 * 1024  # Bound the educational plaintext input to 1 MiB.


def write_new(path, payload):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'wb') as target:
        target.write(payload)


def read_small(path, maximum):
    with open(path, 'rb') as source:
        payload = source.read(maximum + 1)
    if len(payload) > maximum:
        raise ValueError('Use an approved streaming tool for larger data')
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('keygen').add_argument('keyfile')
    sub.add_parser('digest').add_argument('source')
    for operation in ('encrypt', 'decrypt'):
        command = sub.add_parser(operation)
        for argument in ('keyfile', 'source', 'destination', 'context'):
            command.add_argument(argument)
    args = parser.parse_args()
    if args.action == 'keygen':
        write_new(args.keyfile, AESGCM.generate_key(bit_length=256))
        return
    if args.action == 'digest':
        with open(args.source, 'rb') as source:
            print(hashlib.file_digest(source, 'sha256').hexdigest())
        return
    key = read_small(args.keyfile, 32)
    if len(key) != 32:
        raise ValueError('Expected a 32-byte exercise key')
    cipher = AESGCM(key)
    aad = MAGIC + args.context.encode('utf-8')
    if args.action == 'encrypt':
        plaintext = read_small(args.source, LIMIT)
        nonce = os.urandom(12)
        write_new(args.destination, MAGIC + nonce + cipher.encrypt(nonce, plaintext, aad))
    else:
        payload = read_small(args.source, LIMIT + 36)
        if len(payload) < 36 or payload[:8] != MAGIC:
            raise ValueError('Invalid envelope header')
        # Authentication completes before the output file is created.
        plaintext = cipher.decrypt(payload[8:20], payload[20:], aad)
        write_new(args.destination, plaintext)


if __name__ == '__main__':
    try:
        main()
    except (InvalidTag, ValueError, OSError) as error:
        raise SystemExit('Exercise failed: ' + (str(error) or 'authentication tag rejected'))
