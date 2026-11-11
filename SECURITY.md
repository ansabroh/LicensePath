# Security model

All inputs and documents are untrusted. Only the original case sender can assess, append evidence or close. Public reads and registrations are permissionless. No privileged deployer, transfers, external signing, upgrade mechanism or arbitrary external calls exist.

## Evidence

Exact commit URLs, repository binding, byte lengths and SHA-256 prevent mutable branches and silent document substitution. Dependency metadata binds exact name/version to the submitted snapshot. This authenticates selected bytes, not upstream authorship or a registry release. A malicious registrant can supply a misleading inventory or repository. COMPLIANT applies only to that immutable claimed scope.

All document roles are fixed at registration or added once through a bounded challenge; no evidence can be overwritten. The manifest, distribution, versions and requirements never change. Amendments to an existing document require a new case. Challenges add absent roles from the same frozen commit, not a new release. Closure requires the latest hash and does not assert legal compliance.

## Model boundary

Documents are serialized inside an explicitly untrusted DATA section. Instructions inside evidence are not authorized. Models have no contract-created tools, signing access or write capabilities. Schema, enum, identity/order and exact quote checks fail closed. Both leader and independent validators must agree on all decision fields; schema-only or leader-conditioned validation is not used. Exact quotes do not prove correct interpretation. Coordinated model errors, prompt injection and legal ambiguity remain possible, so results are advisory.

## Resource bounds

At most 8 dependencies, 32 files, 16,000 bytes per file and 64,000 declared bytes in total. At most two model attempts per node. Validator review independently re-fetches evidence and validates leader quotations; it therefore performs up to two evidence passes per validator. Cases have one initial assessment and two challenges. Receipts are read individually to avoid unbounded response histories. Unlimited new cases are subject to network fees, not an application-wide quota. Runtime HTTP limits apply; post-fetch length checks do not stop a server transmitting an oversized response.

## Failure semantics

Unavailable, invalid UTF-8 or hash-mismatched evidence yields INCONCLUSIVE when validators agree. Missing license/identity evidence and identity/version mismatch also yield INCONCLUSIVE. Agreed malformed model results fall back to unknown after two attempts. Validator disagreement causes protocol-level undetermined/revert behavior and no new receipt; it must not be represented as successful INCONCLUSIVE. Transaction acceptance/finality does not by itself prove execution success.

## Reporting

Report reproducible, non-sensitive issues through repository issues. Do not include private code, keys, personal records or confidential legal documents: all registered state and external evidence in this design are public.
