# Controlled Mutation Layer (CML) — Python SDK

This is a minimal reference implementation of the **Controlled Mutation Layer**.

It wraps state mutation inside a structured decision boundary and emits a `Turn`.

---

## Why

Modern systems mutate authoritative state:

- Refunds are issued
- Accounts are frozen
- Cases are escalated
- Thresholds change

When behavior shifts, engineers ask:

- Was it model drift?
- Policy drift?
- Threshold adjustment?
- Signal change?

Most systems cannot answer in one query.

CML instruments the mutation boundary so every change becomes explicit.

---

## Atomic Unit: Turn

A Turn captures:

- Pre-state
- Signals
- Policy version
- Decision
- Post-state

If you can’t answer “Why did this change?”, you don’t have a Turn.

---

## Examples

Run:

```bash
python examples/refund_demo.py
