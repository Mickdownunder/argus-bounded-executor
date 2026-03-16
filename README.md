# argus-bounded-executor

[![CI](https://github.com/Mickdownunder/argus-bounded-executor/actions/workflows/tests.yml/badge.svg)](https://github.com/Mickdownunder/argus-bounded-executor/actions/workflows/tests.yml)
[![Release](https://img.shields.io/github/v/tag/Mickdownunder/argus-bounded-executor?label=release)](https://github.com/Mickdownunder/argus-bounded-executor/releases)
[![License: Apache-2.0](https://img.shields.io/github/license/Mickdownunder/argus-bounded-executor)](LICENSE)
[![Stack Setup](https://img.shields.io/badge/docs-stack%20setup-black.svg)](https://github.com/Mickdownunder/operator-control-plane/blob/main/docs/STACK_SETUP.md)

`argus-bounded-executor` is the bounded execution layer in the
`operator-control-plane` stack. ARGUS turns delegated execution requests into
auditable, runtime-bounded attempts with an explicit result contract.

## What ARGUS Does

- Executes bounded plans (`status`, `research`, `full`, `mini`) via
  `bin/argus-research-run`
- Enforces identity binding (mission/dispatch/project) and duplicate-dispatch
  locks
- Delegates validation to ATLAS when needed via `bin/argus-delegate-atlas`
- Emits canonical execution output (`argus_result.json`)

## What ARGUS Does Not Do

- Does not own project truth (Operator does)
- Does not own mission orchestration or dispatch truth (June does)
- Does not act as a planner or policy authority

## Quickstart

1. Configure environment from `.env.example`:

```bash
cp .env.example .env.local
# set ARGUS_WORKSPACE_ROOT, OPERATOR_ROOT, optional JUNE_WORKSPACE_ROOT/ATLAS_WORKSPACE_ROOT
```

2. Run a bounded status path:

```bash
bin/argus-research-run status
```

3. Run tests:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Public Contract

ARGUS publishes `argus_result.json` with mission/dispatch/project identity,
attempt metadata, overall outcome, recommendation, and failure classification.

- Contract spec: `ARGUS_RESULT_CONTRACT.md`
- Reference implementation: `lib/argus_result_contract.py`

## Stack Integration

- Operator: project truth and control-plane authority
- ARGUS: bounded execution attempts
- ATLAS: bounded validation output for executed attempts

Cross-repo wiring and environment conventions:
[operator-control-plane/docs/STACK_SETUP.md](https://github.com/Mickdownunder/operator-control-plane/blob/main/docs/STACK_SETUP.md)
