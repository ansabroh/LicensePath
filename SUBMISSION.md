# LicensePath — Open-Source License Compliance Verification

Contribution type: Builder → Intelligent Contracts.

## Description (under 1,000 characters)

LicensePath is a standalone GenLayer Intelligent Contract for advisory open-source license compliance review. Developers freeze dependency identities, exact versions, license expressions, obligations and distribution conditions. Commit-pinned UTF-8 evidence is checked by SHA-256 and exact byte length. Deterministic logic verifies identity/version metadata and mandatory documents. Leader and validators independently assess full license texts, attribution, notices, source offers and exceptions, validate exact supporting quotations, and agree on per-dependency decision fields. Outcomes are COMPLIANT, CONDITIONAL, CONFLICT or INCONCLUSIVE. Owner-only cases support two bounded append-only evidence challenges, stale-receipt protection, immutable hash-linked receipts and final closure. Includes source, ABI, reproducible fixtures, security documentation and 37 automated SDK direct-mode tests. Assessments cover submitted evidence and are not legally binding advice.

## Evidence

- Repository: https://github.com/ansabroh/LicensePath
- Contract: `contracts/license_path.py`
- ABI: `docs/abi.json`
- Tests: `tests/`; mocked external I/O, with explicitly exercised independent validators.
- SDK: GenVM lint, validation, schema extraction and type checking.
- Live contract: https://explorer-studio.genlayer.com/address/0xed3f4a49f39CcB7b83E194907ab6CdF4460f81A2
- Assessment: `0x4c268d33dbee2435e1bad1fb7f483b00e85981c194b636401aa6dea124139c88`, FINALIZED / SUCCESS; synthetic demo outcome COMPLIANT.
- Full receipt, source hash, screenshot and transaction evidence: `docs/` and `DEPLOYMENT.md`.

No external contribution form was submitted automatically.
