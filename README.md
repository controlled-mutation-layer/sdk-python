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

````bash
python examples/refund_demo.py



## Install

### From GitHub (recommended for now)
pip install "cml @ git+https://github.com/controlled-mutation-layer/sdk-python.git@v0.1.0"

### For contributors (editable)
git clone https://github.com/controlled-mutation-layer/sdk-python.git
cd sdk-python
python -m venv .venv
source .venv/bin/activate
pip install -e .



## Quickstart

Wrap a state mutation so every commit emits a structured `Turn` record.

```python
from cml import Turn  # adjust to your actual public API

# 1) capture "before" state
before = {"refund_policy": "v1", "max_refund": 50}

# 2) apply mutation
after = {"refund_policy": "v2", "max_refund": 75}

# 3) emit a Turn (receipt)
turn = Turn(
    entity_type="policy",
    entity_id="refund_policy",
    action="update",
    before=before,
    after=after,
    actor_type="human",
    actor_id="ops:richard",
    reasons=["policy_update"],
)
print(turn.model_dump())  # or to_json() / dict() depending on your implementation
````
