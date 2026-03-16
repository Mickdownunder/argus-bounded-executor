# Contributing

## Scope

`argus-bounded-executor` is the bounded execution layer. Contributions should
preserve these rules:

- ARGUS is not a global orchestrator.
- Operator owns project truth.
- ARGUS writes bounded local artifacts plus `argus_result.json`.
- Stdout envelope compatibility is part of the public contract.

## Local Checks

Run:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Change Rules

- Do not add arbitrary shell execution paths.
- Prefer environment-variable configuration over hard-coded host paths.
- Keep result-contract compatibility unless you explicitly version the contract.
- Add tests when changing runner guard behavior or contract validation.
