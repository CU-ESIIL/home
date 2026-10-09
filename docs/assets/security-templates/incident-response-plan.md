# Incident response plan

> Planning aid, not a certification or legally sufficient compliance document.
> Complete in an approved private documentation location. Never insert credentials,
> key material, or actual restricted records. Unknown required controls block approval.

- Project / nonsensitive identifier: [fill in]
- Prepared by / accountable owner: [fill in]
- Version / date / next review: [fill in]
- Classification and agreement references: [fill in]
- Approved evidence location: [fill in]

## Contacts and triggers

| Role | Named contact / approved channel | Backup | Notification obligation / deadline |
| --- | --- | --- | --- |
| Institutional security | | | |
| PI / research team | | | |
| Data custodian | | | |
| CyVerse operations | | | |
| VM/cloud operations | | | |
| Privacy/legal/compliance | | | |

- Triggers: unexpected ACL/public release, key/credential compromise, unapproved
  transfer, missing data, failed integrity, unexplained plaintext, suspicious access.
- Who may declare an incident and authorize containment: [fill in]
- Immediate reporting route; do not send restricted records in tickets: [fill in]

## Response sequence

1. Record time, affected system/version, and observation without spreading data.
2. Notify institutional security and designated project contact through approved channels.
3. Preserve authorized evidence and logs; avoid destroying evidence during cleanup.
4. Under authorized direction isolate sessions/routes, suspend access, rotate or
   revoke affected credentials/keys, and inventory data/replicas/snapshots.
5. Determine scope with providers and custodian; institution coordinates required
   legal/contractual notifications and deadlines.
6. Restore only after integrity and authorization review; document corrective actions.

- Evidence custody, access, timestamps and approved storage: [fill in]
- Key compromise and historical ciphertext response: [fill in]
- Notification templates and contractual references: [fill in]
- Tabletop exercise, lessons and next test: [fill in]

## Review and authorization

- Unresolved controls / remediation owner / due date: [fill in]
- Exceptions, approving authority, scope, and expiry: [fill in]
- Custodian decision / date / evidence reference: [fill in]
- Institutional decision / date / evidence reference: [fill in]
- Provider confirmation references: [fill in]
- Material changes requiring revalidation: [fill in]

For each control, record **Supported**, **Configured**, **Verified**, and
**Approved** separately, with dates and evidence. Do not mark unknown as passed.
