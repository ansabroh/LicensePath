# Deployment and verification

## Current instance

- Network: GenLayer Studio / Studionet sandbox (not mainnet).
- Contract: `0xed3f4a49f39CcB7b83E194907ab6CdF4460f81A2`.
- Explorer: https://explorer-studio.genlayer.com/address/0xed3f4a49f39CcB7b83E194907ab6CdF4460f81A2
- Deployment transaction: `0x9e3b980003a001cd8ece1346d09013873c062851d4ed2bffb384a30312038dad`.
- Deployment observed finalized and contract methods exposed in Studio.
- Account: Studio built-in account; no MetaMask or exported private key used.
- Execution mode: Normal (Full Consensus), Simulation Mode off.
- Demo registration and assessment transactions are listed in `docs/deployment.json` after verification.
- Demo case ID: `3e7403c49ba484d54ebed9db6cfba1e7f1d63d0f2df524193777cbbaaea3914f`.

Live assessment: `0x4c268d33dbee2435e1bad1fb7f483b00e85981c194b636401aa6dea124139c88`, FINALIZED / SUCCESS, advisory outcome **COMPLIANT**. The leader and three agreeing validators reached majority consensus; one validator disagreed and another was cancelled after quorum. This is majority consensus, not a claim of unanimity. These fixtures are synthetic package documents, not a third-party licensing audit. Studio is resettable and its addresses may cease to resolve after a network reset.

## Reproduce in Studio

1. Import `contracts/license_path.py`.
2. Open Run and Debug; leave Normal (Full Consensus) selected and simulation off.
3. Deploy with no constructor parameters.
4. Call `register` using the two JSON string values from `fixtures/studio-register-args.json`.
5. Verify execution SUCCESS and save the returned case ID.
6. Call `assess(case_id)`. Wait for acceptance/finality and inspect execution result separately.
7. Read `get_receipt(case_id, 1)` and `get_case(case_id)` from the deployed instance.
8. To exercise a challenge, register a separate case using `fixtures/evidence-missing-attribution.json`, assess, then call `challenge` using the latest `receipt_hash`, a reason and `fixtures/challenge-attribution.json` as a JSON string. Closure similarly requires the latest hash.

No retries should mutate existing registrations. If a receipt does not exist after a failed/undetermined transaction, inspect protocol execution details before retrying. A stored INCONCLUSIVE outcome is an agreed advisory finding, not a protocol error.

## Local checks

```sh
pip install -r requirements-dev.txt
python -m pytest
genvm-lint check contracts/license_path.py
genvm-lint typecheck contracts/license_path.py
genvm-lint schema contracts/license_path.py --output /tmp/abi.json
diff docs/abi.json /tmp/abi.json
```

Automated tests use the actual pinned GenLayer SDK storage and official `gltest.direct` runtime. Web/LLM I/O is mocked. Validators are invoked explicitly because the direct-mode runner captures validator closures without automatically executing network consensus. The suite checks acceptance and deliberate disagreement, but cannot establish model accuracy or live quorum reliability.

## Release verification notes

The initial development instance returned agreed INCONCLUSIVE because complete attribution quotes exceeded an overly short quote limit. The release accepts exact document quotations up to 4,000 characters, with a 20,000-byte total model-result bound, and includes a regression test for the complete MIT notice. License quotes remain bounded to 800 characters.

Tests explicitly pin the SDK release `v0.2.16`, matching the contract dependency hash, and CI pre-downloads it. This avoids the testing tool selecting an incompatible latest prerelease asset on a clean machine.

## Saved evidence

- `docs/live-receipt.json`: exported finalized assessment output, verified against the immutable manifest and evidence hashes.
- `docs/finalized-assessment.png`: Studio screenshot showing FINALIZED / SUCCESS and the COMPLIANT output.
- `docs/deployment.json`: source SHA-256, deployment/registration/assessment transaction IDs and development-instance history.
- All 37 tests plus lint, SDK validation, type checking, ABI consistency and reproducible fixtures passed on GitHub Actions.

Verify the saved receipt locally:

```sh
python scripts/verify_receipt.py docs/live-receipt.json fixtures/manifest.json
```

Successful hash verification confirms integrity relative to these inputs; use the public explorer and deployed contract as the trusted source for origin.

Demo closure: `0xfea1ae0b3033735f44b8145f6d0d98ad26634291cf34054e507969d8d0cf9bfb`, FINALIZED / SUCCESS. The final instance has four successful finalized transactions: deploy, register, assess and close. The demo case is now closed; create a new case to try challenges.
