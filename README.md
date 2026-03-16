# argus-bounded-executor

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Stack Setup](https://img.shields.io/badge/docs-stack%20setup-black.svg)](https://github.com/Mickdownunder/operator-control-plane/blob/main/docs/STACK_SETUP.md)

Kurz auf Deutsch: `argus-bounded-executor` ist die begrenzte
Ausfuehrungsschicht des Stacks. ARGUS fuehrt delegierte Arbeit unter klaren
Laufzeit-, Identitaets- und Dispatch-Grenzen aus und liefert ein sauberes
Ergebnisartefakt an Operator zurueck.

`argus-bounded-executor` is the bounded execution layer of the public stack.
ARGUS does not own project truth or planning authority. Its job is to turn a
delegated execution request into a controlled attempt with explicit identity
binding, runtime boundaries, and a canonical result contract that Operator can
ingest.

## What ARGUS Actually Does

ARGUS exposes bounded execution entrypoints such as:

- `bin/argus-research-run`
- `bin/argus-delegate-atlas`

Those entrypoints:

- accept a bounded plan such as `status`, `research`, `full`, or `mini`
- validate mission, dispatch, and optional project bindings
- acquire dispatch locks to prevent duplicate active execution
- run Operator entrypoints under bounded runtime control
- optionally delegate the validation leg to ATLAS
- emit a canonical `argus_result.json` artifact for Operator and higher layers

## Design Goals

ARGUS exists so execution can be aggressive without becoming sovereign.

It is intentionally constrained:

- June owns mission truth and dispatch truth
- Operator owns project truth
- ARGUS owns execution-local attempts and attempt-local artifacts only

That boundary is the point.
ARGUS can do real work, recover from stale dispatch locks, and carry enough
identity to be auditable, but it is not allowed to become a second planner.

## What Is In This Repository

- bounded execution entrypoints
- result-contract generation
- delegation glue from ARGUS to ATLAS
- execution safety checks around identity and duplicate dispatch
- tests for the public contract surface

## Result Contract

The main public output is `argus_result.json`.

That contract records things such as:

- mission and dispatch identity
- bound project identity when present
- attempt identity and run directory
- overall execution outcome
- recommendation and failure classification
- downstream ATLAS outcome when validation was delegated

See:

- `ARGUS_RESULT_CONTRACT.md`
- `lib/argus_result_contract.py`

## Configuration

Copy `.env.example` into your local environment management and set:

- `ARGUS_WORKSPACE_ROOT`
- `OPERATOR_ROOT`
- optionally `JUNE_WORKSPACE_ROOT`
- optionally `ATLAS_WORKSPACE_ROOT`

## Test

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## How It Fits Into The Stack

ARGUS is most useful as the execution arm of Operator, not as a standalone
agent product.

- Operator decides what project state means
- ARGUS performs bounded execution attempts
- ATLAS validates or challenges those attempts

For cross-repo wiring and environment variables, see:
[operator-control-plane/docs/STACK_SETUP.md](https://github.com/Mickdownunder/operator-control-plane/blob/main/docs/STACK_SETUP.md)
