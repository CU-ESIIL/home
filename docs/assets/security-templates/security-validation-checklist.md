# Security validation checklist

> Planning aid, not a certification or legally sufficient compliance document.
> Complete in an approved private documentation location. Never insert credentials,
> key material, or actual restricted records. Unknown required controls block approval.

- Project / nonsensitive identifier: [fill in]
- Prepared by / accountable owner: [fill in]
- Version / date / next review: [fill in]
- Classification and agreement references: [fill in]
- Approved evidence location: [fill in]

## Test record

Use synthetic records and authorized test accounts. A pass is scoped to the tested
configuration and does not establish formal certification.

| Control | Procedure | Expected | Actual / pass, fail, unknown | Tester / date | Evidence | Remediation owner / due |
| --- | --- | --- | --- | --- | --- | --- |
| Storage ACLs/groups/tickets | Inspect parents and new objects; permitted and non-member read/write tests | Intended access only | | | | |
| Storage encryption | Obtain scoped backend/replica evidence and file encryption test | Required coverage evidenced | | | | |
| Replication and recovery | Restore synthetic object; compare trusted reference | Required copies and recovery work | | | | |
| Retention | Check trash, backups, holds and deletion process | Approved deadlines apply to every copy | | | | |
| Transfer auth and TLS | Check actual auth path and effective settings; approved bad-cert test; data-channel evidence | Bad peer denied, required channels encrypted | | | | |
| Transfer integrity | Checksum round trip, compare reference, tamper test | Bytes match; authenticated decrypt rejects tamper | | | | |
| VM access and MFA | Test notebook/SSH/API auth and session expiry | Only approved entry routes/users | | | | |
| VM encryption/swap/snapshots | Inventory actual volumes; inspect configuration/provider evidence | Plaintext persistence matches plan | | | | |
| Container isolation | Inspect UID, mounts, capabilities, image digest and daemon exposure | Approved runtime only | | | | |
| Network | Test allowed and blocked ingress/egress | Required routes only | | | | |
| Key access and recovery | Authorized/unauthorized release and exercise recovery/revocation | Least privilege plus recovery | | | | |
| Processing residues | Scan synthetic marker after success, crash and cancel in temp/logs/cache/layers | No unexplained plaintext copies | | | | |
| Outputs | Disclosure review, encrypt, restore, compare, inspect ACL | Authorized output and correct preservation | | | | |
| Cleanup | Inventory files, snapshots, backups, trash after cleanup | Retained exceptions approved | | | | |
| Credentials/sessions | Terminate and revoke exercise access; test old session | Old access unusable | | | | |

## Four-state register

| Control id | Supported evidence | Configured evidence | Verified test id/date | Approved authority/scope/date |
| --- | --- | --- | --- | --- |
| [fill in] | | | | |

## Review and authorization

- Unresolved controls / remediation owner / due date: [fill in]
- Exceptions, approving authority, scope, and expiry: [fill in]
- Custodian decision / date / evidence reference: [fill in]
- Institutional decision / date / evidence reference: [fill in]
- Provider confirmation references: [fill in]
- Material changes requiring revalidation: [fill in]

For each control, record **Supported**, **Configured**, **Verified**, and
**Approved** separately, with dates and evidence. Do not mark unknown as passed.
