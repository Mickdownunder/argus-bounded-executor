# Argus Control-Plane Ownership

Argus is a bounded execution subsystem under June.

It may write:
- local logs
- local run artifacts
- local summaries
- bounded result contracts

It may not write:
- June mission truth
- Operator project truth
- global Operator control-plane events

Global nuance should flow through contract fields, not new global event types.
