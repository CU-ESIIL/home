# Encryption and key management plan

> Planning aid, not a certification or legally sufficient compliance document.
> Complete in an approved private documentation location. Never insert credentials,
> key material, or actual restricted records. Unknown required controls block approval.

- Project / nonsensitive identifier: [fill in]
- Prepared by / accountable owner: [fill in]
- Version / date / next review: [fill in]
- Classification and agreement references: [fill in]
- Approved evidence location: [fill in]

## Encryption coverage

| Layer / data copy | Algorithm / format / version | Who holds keys | Configured scope | Test / evidence | Gap |
| --- | --- | --- | --- | --- | --- |
| Transfer / control and data channels | | | | | |
| Data Store files and backend | | | | | |
| VM scratch / swap | | | | | |
| Replicas / snapshots / backups | | | | | |
| Restricted outputs | | | | | |

## Key lifecycle (identifiers only)

- Generator and approved cryptographic/module requirements: [fill in]
- Key id, custodian, vault/service and separation from data: [fill in]
- Authorized release and runtime exposure: [fill in]
- Nonce/IV requirements and authenticated format: [fill in]
- Integrity, sender authenticity, and rollback protection: [fill in]
- Cryptoperiod, rotation trigger, and old-copy re-encryption: [fill in]
- Recovery custodian, escrow authorization, and recovery test: [fill in]
- Compromise response, revocation and copied-key risks: [fill in]
- Final destruction, retained key copies, and evidence: [fill in]
- GoCommands mode limitations if used: [fill in]

## Review and authorization

- Unresolved controls / remediation owner / due date: [fill in]
- Exceptions, approving authority, scope, and expiry: [fill in]
- Custodian decision / date / evidence reference: [fill in]
- Institutional decision / date / evidence reference: [fill in]
- Provider confirmation references: [fill in]
- Material changes requiring revalidation: [fill in]

For each control, record **Supported**, **Configured**, **Verified**, and
**Approved** separately, with dates and evidence. Do not mark unknown as passed.
