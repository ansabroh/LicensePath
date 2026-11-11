# Evidence format

See `fixtures/manifest.json` and `fixtures/evidence.json` for complete concrete inputs. Public methods accept JSON **strings**, not nested calldata objects.

A manifest has exactly `project`, `distribution`, `conditions`, `dependencies`. A source has `repo` (`owner/repository`) and `commit` (40 lowercase hexadecimal characters). Distribution is `source`, `binary`, `saas`, or `internal`. Each dependency has exactly `id`, exact `version`, declared `license` expression, `source`, free-text `requirements`, and `mandatory` document roles. Conditions must explain linking, modifications, distribution restrictions and relevant operating facts; unknown facts should lead to INCONCLUSIVE.

Each evidence descriptor contains exactly:

```json
{
  "id": "license",
  "dependency": "licensepath-demo-lib",
  "role": "license",
  "url": "https://raw.githubusercontent.com/ansabroh/LicensePath/ca423e1d1986b595011f7a8957da0f9dc278d6d9/fixtures/demo-license.txt",
  "sha256": "COPY_THE_EXACT_VALUE_FROM_fixtures/evidence.json",
  "bytes": 0
}
```

The example above describes fields only; the placeholder hash and zero bytes are intentionally invalid. Use generated fixture values for transactions. Roles: `metadata`, `license`, `attribution`, `notice`, `source_offer`, `exception`. At most one file for each dependency and role. Combine multiple notices into one commit-pinned UTF-8 file where necessary; preserve original contents. Metadata must be exactly a JSON object with `name` and `version`, and must match the dependency registration. It is a normalized identity document, not proof of registry provenance.

Obligation review covers the complete supplied license, including missing requirements, OR branch selection, AND obligations and applicable exceptions. A non-unknown semantic status needs a contiguous 20–800 character license quotation. Satisfied/conflict statuses additionally need at least one grounded non-license/non-metadata document quotation. Document quotes are bounded to 20–4,000 characters. Every document quote is checked against a file for the same dependency. Reasons are bounded to 1,000 characters and quote counts to six. Grounding verifies byte-derived text occurrence, while independent reasoning checks relevance.

Receipt hashes use Python `json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)` encoded as UTF-8, then SHA-256. No floats are admitted by the schemas. To verify a receipt, remove only `receipt_hash`, recompute its hash, verify `manifest_hash`, `evidence_hash` and `previous_hash`, and obtain the next sequence directly from the same deployed contract. Sequence 1 starts with 64 zero characters. This chain detects alteration relative to a trusted chain head; it is not a separate digital signature.
