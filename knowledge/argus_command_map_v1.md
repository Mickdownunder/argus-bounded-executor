# ARGUS Command Map v1

## Approved command macro

- `bin/argus-research-run <status|research|full> [request text]`

## Internal mapped wrappers used by macro

- `$OPERATOR_ROOT/bin/oc-healthcheck`
- `$OPERATOR_ROOT/bin/oc-job-status 20`
- `$OPERATOR_ROOT/bin/oc-research-init [request text]`
- `$OPERATOR_ROOT/bin/oc-research-cycle [request text]`

No other execution paths are permitted for autonomous ARGUS runs.

## Sandbox Validation Delegation (ATLAS)

Preferred ARGUS delegation entrypoint:

- `bin/argus-delegate-atlas <status|research|full> [request text]`

Rules:

- For safety-critical validation, ARGUS delegates to ATLAS.
- ATLAS returns deterministic evidence paths + recommendation.
- ARGUS escalates promotion decisions to June/Master.
