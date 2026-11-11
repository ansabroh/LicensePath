# LicensePath

A standalone GenLayer Intelligent Contract for evidence-backed open-source license compliance assessments. Developers freeze a dependency inventory, exact versions, license expressions, declared obligations and distribution conditions. GenLayer validators independently retrieve pinned documents and assess applicable license obligations. Results are advisory, never legally binding.

## Outcomes

| Outcome | Meaning |
| --- | --- |
| COMPLIANT | All supplied dependencies have complete applicable-obligation coverage and grounded satisfaction; mandatory documents exist. |
| CONDITIONAL | Evidence establishes curable obligations or missing declared mandatory documents. |
| CONFLICT | Independent semantic review finds an explicit, grounded incompatibility with the declared distribution conditions. |
| INCONCLUSIVE | Unavailable/altered evidence, version/identity mismatch, ambiguous applicability, incomplete obligation coverage, or invalid model response. |

Unknown evidence takes precedence. A version mismatch means the supplied evidence does not establish this dependency, so it is INCONCLUSIVE rather than a licensing violation. Empty inventories are rejected. A result only covers the registered inventory; it cannot prove there are no undeclared dependencies.

Live Studio deployment: [`0xed3f…81A2`](https://explorer-studio.genlayer.com/address/0xed3f4a49f39CcB7b83E194907ab6CdF4460f81A2). The synthetic demo assessment finalized successfully with **COMPLIANT** under full consensus. [Saved receipt](docs/live-receipt.json) and [deployment evidence](DEPLOYMENT.md).

## Quick start

Requires Python 3.12+ and internet access for the pinned GenVM SDK download.

```sh
pip install -r requirements-dev.txt
python -m pytest
genvm-lint check contracts/license_path.py
genvm-lint typecheck contracts/license_path.py
genvm-lint schema contracts/license_path.py --output /tmp/abi.json
python scripts/prepare_demo.py
```

37 direct-mode SDK tests cover all outcomes, owner isolation, malformed inputs and responses, citation grounding, byte/hash failures, immutable state, challenge bounds, stale receipts, independent-validator disagreement and receipt integrity. External web and LLM responses are mocked in those tests; they do not establish real-model legal accuracy or production consensus. See [DEPLOYMENT.md](DEPLOYMENT.md) for live validation status.

## Contract API

Import `contracts/license_path.py` into [GenLayer Studio](https://studio.genlayer.com), use the built-in account, select **Normal (Full Consensus)**, and deploy with no constructor arguments.

| Method | Access | Purpose |
| --- | --- | --- |
| `register(manifest_json, evidence_json)` | Anyone | Create an immutable case scoped to the sender and return its SHA-256 ID. |
| `assess(case_id)` | Case owner | First evidence retrieval and independent consensus assessment. |
| `challenge(case_id, expected_receipt, reason, additional_evidence_json)` | Case owner | Append new evidence roles; at most two further assessments. |
| `close(case_id, expected_receipt)` | Case owner | Freeze the latest receipt, regardless of advisory outcome. |
| `get_case(case_id)` | Public | Registration, owner, assessment count, closed state. |
| `get_receipt(case_id, sequence)` | Public | One immutable receipt; sequence starts at 1. |

Use the two string values in `fixtures/studio-register-args.json` as `register` arguments. Store the returned case ID. Call `assess`, then inspect `get_receipt(case_id, 1)` and execution success, not merely transaction acceptance. A full receipt contains all evidence descriptors, manifest/evidence hashes, per-dependency findings, grounded quotes, deterministic issues, previous receipt hash and its own hash.

## Why GenLayer is central

Deterministic code handles exact identities, versions, mandatory file presence, inputs and history. It cannot decide whether an exception actually applies, whether attribution preserves the relevant notices, whether a source offer meets the license wording, or whether declared conditions conflict with the full license. Those are the nondeterministic semantic task.

`gl.vm.run_nondet_unsafe` runs a leader and a custom validator. Every validator independently fetches and hashes evidence, checks identities and runs the same task without seeing the leader's answer. It validates the leader's citation schema and exact quotations, then compares dependency IDs, obligation-coverage flags, semantic statuses, deterministic issues and the derived aggregate. Wording and quote selection may differ; the decision fields must agree. Failed network consensus leaves no new receipt; it is distinct from an agreed INCONCLUSIVE assessment.

## Immutable evidence and limits

- HTTPS `raw.githubusercontent.com` only; full 40-character lowercase commit pins, safe repository-relative paths, no query strings or traversal.
- License and metadata files must be from the registered dependency repository/revision. Distribution evidence must be from the registered project revision.
- SHA-256 and exact original UTF-8 byte counts are checked after each fetch. No newline normalization, rendering, arbitrary hosts or tool-followed links.
- 1–8 dependencies, 1–32 evidence files, 16 KB per file, 64 KB total evidence, 2 model attempts per node, maximum 3 receipts per case.
- Evidence is append only and one file per dependency/role. Fixing existing files or changing a release needs a new case. Missing roles can be appended from the same frozen project commit; they must already exist there.
- Metadata is an explicit normalized JSON identity document containing exactly `name` and `version`; this contract does not parse arbitrary lockfile formats or authenticate package-registry ownership.
- Declared source repositories and inventories are submitter claims. Commit/hash authentication proves byte identity, not authorship, rights ownership, build contents or provenance.
- Size checks bound bytes admitted to reasoning and storage. The web runtime may download the whole HTTP response before checking its length; there is no claim of transport streaming limits or contract-configured HTTP timeouts.

## Reproducible fixtures

`fixtures/demo-*` are clearly synthetic MIT-licensed package documents, pinned at commit `ca423e1d1986b595011f7a8957da0f9dc278d6d9`. They are not an audit of an external package. `scripts/prepare_demo.py` computes exact descriptors and Studio arguments without credentials. Start a second case with `evidence-missing-attribution.json` to exercise a missing-document assessment, then append `challenge-attribution.json`. Results still depend on independent model review; no outcome is forced in production.

[Evidence format](EVIDENCE.md) · [Security model](SECURITY.md) · [Deployment](DEPLOYMENT.md) · [Submission text](SUBMISSION.md) · [ABI](docs/abi.json)

## Official references

- [GenLayer Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle)
- [Calling LLMs](https://docs.genlayer.com/developers/intelligent-contracts/features/calling-llms)
- [Persistent storage](https://docs.genlayer.com/developers/intelligent-contracts/storage)
- [Web access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access)
- [GenVM linter](https://docs.genlayer.com/api-references/genlayer-linter)

The source pins the SDK runner in its dependency header. The SDK's actual `Response.status` field and explicit `response_format='json'` were checked against the installed runner and direct-mode execution. Documentation examples can target a different SDK generation.

MIT licensed. No frontend, token, payment handling or automatic legal enforcement is included.
