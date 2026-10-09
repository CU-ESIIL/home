---
title: Sensitive Data Guide — Technical Verification Report
description: Source verification, validation evidence, and unresolved deployment controls for the OASIS sensitive-data guide.
date: 2026-10-09
---

# Sensitive data guide: technical verification report

Verification date: **2026-10-09**. Scope: documentation and synthetic local examples. This is not a security assessment of a live CyVerse, OASIS, or VM deployment. Read [Working with Sensitive and Restricted Data](../quickstart/sensitive-data.md) for the workflow and approval gates.

## Files created

- `docs/quickstart/sensitive-data.md`: comprehensive guide, approval process, lifecycle, encryption analysis, tutorial, hardening, linkage, validation and shared responsibility.
- `docs/assets/diagrams/sensitive-data/secure-triangle.svg`, `data-lifecycle.svg`, `security-boundaries.svg`: three maintainable diagrams with titles, descriptions, alt text and prose equivalents.
- `docs/assets/security-templates/`: ten Markdown worksheets, `synthetic-envelope.py` educational helper, and downloadable `oasis-security-templates.zip` containing the raw worksheets and helper.
- `docs/dev/sensitive-data-verification.md`: this report.
- `scripts/package_security_templates.py`: deterministic ZIP packager. After editing template/helper sources, run `python3 scripts/package_security_templates.py` and commit the rebuilt ZIP.

## Files modified

- `mkdocs.yml`: existing Resources navigation includes the guide; the notebook plugin leaves the downloadable helper as a raw Python file.
- `docs/overrides/partials/cloud_container_page.html`, `quickstart_page.html`, and `directory/infrastructure_page.html`: guide cards in Cloud Container, Quick Start, and the infrastructure documentation gallery, using an existing thumbnail; no image generation or replacement.
- `docs/resources/index.md`: Resources hub link.
- `docs/quickstart/cloud.md`, `python.md`, `cyverse.md`, `data-library/index.md`, and `docs/resources/cyverse_move_and_save_data.md`: contextual restricted-data links.
- Generated tag pages rebuilt through `scripts/generate_tags.py`; source front matter remains authoritative.
- `PROMPT_LOG.md`: concise record of the work, checks, and unresolved controls.

No homepage layout or CSS change. No registry entry: the addition is a procedural guide, not a new ecosystem entity.

## Claims checked directly against source

Public upstream GoCommands repository cloned and inspected at commit
[`a5109339b174c7defca644a3c10a9fa0ed1f66de`](https://github.com/cyverse/gocommands/tree/a5109339b174c7defca644a3c10a9fa0ed1f66de), with `VERSION.txt` reporting v0.12.5. This pins the reviewed source, not the version installed by every researcher.

| Claim | Source inspected / finding |
| --- | --- |
| Encryption modes | `commons/encryption/encryption.go`, `cmd/flag/encryption.go`: `ssh`, `winscp`, `pgp`; no native GCM mode. |
| Encryption enablement | `--encrypt` defaults false; key flag can enable it; metadata mode lookup exists; `--no_encrypt` overrides it. |
| Decryption | `--decrypt` defaults true; `--no_decrypt` overrides. Reviewed `get` and `ls` support explicit key/temp options. |
| SSH content encryption | `encryption_ssh_rsa.go`: random 32-byte key, random 16-byte IV, RSA-OAEP with SHA-256 wrapping, AES-CTR body. |
| Content integrity | `encryption_aes.go` uses `cipher.NewCTR`; SSH and WinSCP body paths have no MAC/tag. RSA header wrapping does not authenticate the body. |
| SSH filename exposure | Filename key is taken from public RSA modulus bytes. Obfuscation is not confidentiality against a public-key holder. |
| WinSCP | Supplied key bytes and random IV; CTR for names/content; helper pads keys rather than applying a password-strengthening KDF. |
| PGP | `encryption_pgp.go`: symmetric OpenPGP AES-256, original name plus suffix, no sender-signature generation; consumes `UnverifiedBody` through EOF. The pinned `golang.org/x/crypto` v0.43.0 dependency emits SHA-1 MDC and checks it at EOF; the helper writes plaintext before that final check. Not represented as GCM or authenticate-before-output. |
| Key parsing | `encryption_ssh.go`: existing RSA key material, no support for passphrase-encrypted private keys in reviewed parser. |
| Commands | Manuals and Cobra flag definitions for init/env/ls/mkdir/chmod/chmodinherit/put/get; `-k`, `-A`, `-L`, encryption/decryption and temp flags checked. |
| Configuration | Versioned manual supports negotiation, client policy, hostname verification and CA environment variables; environment precedence is documented. |

GoCommands pins `go-irodsclient` **v0.21.4** in `go.mod`. That dependency was separately inspected at commit
[`b13692a7c5f7fbddb7e0ed24d68ad3005b6f8020`](https://github.com/cyverse/go-irodsclient/tree/b13692a7c5f7fbddb7e0ed24d68ad3005b6f8020).
`irods/types/ssl_config.go` enables normal Go TLS certificate verification only for `hostname`; other values, including `cert`, set `InsecureSkipVerify`. The guide uses `hostname` and requires deployment tests. Negotiation settings alone do not prove every data route is encrypted or meets institutional protocol/cipher requirements.

CyVerse's [access management documentation](https://learning.cyverse.org/ds/gocommands/access_management/) corroborates ACL inspection and user/group access commands. [iRODS documentation source](https://github.com/irods/irods_docs) is linked for platform background rather than treating general iRODS capabilities as enabled CyVerse policies.

The OpenPGP dependency was checked directly at [`golang/crypto` v0.43.0](https://github.com/golang/crypto/tree/v0.43.0), commit `627cb894b6b2021e34c4ad4af4c0a963127491e4`: `openpgp/write.go`, `read.go`, and `packet/symmetrically_encrypted.go` confirm MDC emission and EOF validation. A failed PGP decrypt can expose partially written plaintext before rejection; the guide states this limitation.

## Claims requiring confirmation from CyVerse

All remain **unconfirmed for a project-specific deployment**:

- Permitted data classifications and agreement compatibility; actual storage/service locations.
- Authentication scheme, MFA coverage for browser and CLI, ticket/public-sharing behavior, effective groups and administrator access.
- Backend encryption and key custody; encryption of all replicas and backups.
- Transfer endpoint certificates, secure negotiation, resource/data-channel encryption, supported protocols/ciphers and routes.
- Replication policy, failure domains, backup coverage, restore process and recovery objectives.
- Audit event coverage, access to logs, retention and incident notification obligations.
- Trash, backup and replica deletion timelines, holds, and evidence for destruction.

## Claims requiring confirmation from VM/cloud or hosted-app provider

All remain **unconfirmed for the proposed instance/app**:

- Hosting provider/region, allowed classifications, administrative and hypervisor access, tenancy and isolation.
- MFA and all notebook/SSH/API access paths; guest and cloud network rules, egress enforcement.
- Working-volume/swap encryption, memory/dump exposure, keys, snapshots, images and backup retention.
- Ability to set user, mounts, capabilities, read-only roots, image provenance, patches and network policy for the actual container route.
- Audit coverage, support access, incident response, shutdown versus volume deletion and destruction evidence.

## Remaining institutional and custodian approval requirements

Classify inputs, linkage keys, joins, and outputs; identify contractual, privacy,
legal and institutional requirements; decide whether named OASIS components are
permitted; resolve required control gaps; approve users/purposes, key custody,
retention, incident response and disclosure rules. Obtain written authorization
before uploading restricted data. Some classifications require another designated
environment. No certification of OASIS, CyVerse or Jetstream2 is asserted.

## Validation evidence and limitations

- Local educational envelope tested with Python and `cryptography` 50.0.2: input and output round trips, tamper rejection, wrong key/context rejection with no plaintext destination, exclusive writes, 0600 key creation, fresh random nonces, empty input and size-limit rejection.
- Synthetic aggregation yields region A: n=2, mean=13.0; region B: n=2, mean=10.0. These counts are instructional, not disclosure thresholds.
- GoCommands syntax is source-verified. No live authentication, upload, ACL mutation, TLS negative test, provider hardening, or restricted-data transaction was performed. These tests remain required in an authorized project-specific synthetic exercise.
- Strict site build: `.venv/bin/python -m mkdocs build --strict` passed. Initial validation identified the missing report and the notebook plugin trying to render the helper; both were corrected before the successful build.
- Existing Playwright suite: **8 passed**, covering homepage structure, mobile overflow, theme, navigation/history, galleries, images and links.
- Additional local Chromium checks: guide at **1280, 375, and 320 pixels**, no document horizontal overflow; all three diagrams loaded; no SVG text outside viewBox; desktop/mobile screenshots visually reviewed.
- **173 internal link/download checks** across the guide, Cloud Container, Resources, contextual guides and this report returned HTTP 200; same-page targets resolved. Full-size diagram links resolved in the final run.
- Accessibility fundamentals: English language set, one main h1, nonempty link names, table column headers, meaningful diagram alt text and SVG title/description, prose equivalents, and keyboard-operable expandable sections. This was a focused check, not a full WCAG conformance audit.
- **11 Bash blocks** parsed with `bash -n`; the synthetic Python aggregation was executed, and the educational helper negative tests passed. Docker and native GoCommands snippets remain source/documentation-checked, configuration-dependent examples.
- Front matter checker passed for the new guide and changed curated pages. Tag generator ran; lowercase `cyverse` avoids a case collision with the existing tag page. Regeneration also refreshed two existing schedule-title labels.
- Downloadable ZIP verified to contain exactly ten raw Markdown templates and the Python helper, matching their source bytes; an unchanged packager rebuild produces the same ZIP hash. Site search includes the guide. The helper URL returns raw Python, not a rendered notebook.
- Original external technical references were opened through browsing or inspected in their public source repositories. The iRODS docs host could not be retrieved by the browsing tool, so the original documentation source repository is linked instead.
- Content review found no real credentials, private keys, tokens or restricted records: examples use placeholders and four synthetic records. No restricted service was accessed and no deployment certification or blanket authorization is asserted.

## Review from three perspectives

- **Researcher:** classification leads to an environment decision before setup; each lifecycle stage identifies risk, protections, tests and retained evidence. Synthetic commands and reusable worksheets provide a concrete starting point.
- **Infrastructure engineer:** transfer/control channels, file encryption, administrator access, container/VM boundaries, plaintext residues and destruction are distinct. Commands are source-checked and live controls remain unconfirmed.
- **Research security reviewer:** supported/configured/verified/approved are separate states; provider commitments, classification, agreements, named users, retention, incident response and disclosure require evidence and authorization. Required gaps block restricted processing.

The documentation deliverables are complete. Project-specific provider confirmations and institutional approvals remain prerequisites for actual restricted-data use.
