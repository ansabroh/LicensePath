# Deployment and verification

## Current instance

- Network: GenLayer Studio / Studionet sandbox (not mainnet).
- Contract: `0x35408353C5f7b85F23653473AE578De5Debd8790`.
- Explorer: https://explorer-studio.genlayer.com/address/0x35408353C5f7b85F23653473AE578De5Debd8790
- Deployment transaction: `0x6f571506bd3ee5443da94ee1653ef8bf141ebf64e187ab3599037ba7eda963f4`.
- Deployment observed finalized and contract methods exposed in Studio.
- Account: Studio built-in account; no MetaMask or exported private key used.
- Execution mode: Normal (Full Consensus), Simulation Mode off.
- Demo registration: `0x369742e0bd0c048f09ed81edd5e971a700c2a7ab4505236762ad4a15736453d8`, FINALIZED / SUCCESS.
- Demo case ID: `3e7403c49ba484d54ebed9db6cfba1e7f1d63d0f2df524193777cbbaaea3914f`.

Live assessment details are recorded below after verification. These fixtures are synthetic package documents, not a third-party licensing audit. Studio is resettable and its addresses may cease to resolve after a network reset.

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
