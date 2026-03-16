# Argus Workspace

Argus is a bounded June-owned research executor. This workspace owns only local run artifacts,
summaries, and the canonical Argus result contract.

## Canonical entrypoints
- `bin/argus-research-run`
- `bin/argus-delegate-atlas`

## Configuration

Copy `.env.example` into your local environment management and set:

- `ARGUS_WORKSPACE_ROOT`
- `OPERATOR_ROOT`
- optionally `JUNE_WORKSPACE_ROOT`
- optionally `ATLAS_WORKSPACE_ROOT`

## Ownership boundaries
- June owns mission, dispatch, and escalation truth.
- Operator owns project truth.
- Argus writes only bounded attempt artifacts and `argus_result.json`.

## Contracts
- `ARGUS_RESULT_CONTRACT.md`
- `lib/argus_result_contract.py`

## Tests
Run:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Full-Stack Wiring

For cross-repo wiring and environment variables, see the Operator stack guide:
[operator-control-plane/docs/STACK_SETUP.md](https://github.com/Mickdownunder/operator-control-plane/blob/main/docs/STACK_SETUP.md)
