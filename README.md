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

`pre_state` and `post_state` describe what changed.
`signals` carries bounded metadata (actor, reason codes, correlation ids, etc.) describing why and how the mutation occurred.

Wrap a state mutation so every commit emits a structured `Turn` record.

```python
import datetime
from uuid import uuid4
from cml.turn import Turn

# 1) capture "before" state
pre_state = {"refund_policy": "v1", "max_refund": 50}

# 2) apply mutation
post_state = {"refund_policy": "v2", "max_refund": 75}

# 3) emit a Turn (receipt at the mutation boundary)
turn = Turn(
    turn_id=str(uuid4()),
    timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    pre_state=pre_state,
    signals={
        "entity": "refund_policy",
        "actor": "ops:test",
        "reason_codes": ["policy_update"],
    },
    policy_version="v0",
    decision="update_refund_policy",
    post_state=post_state,
)

print(turn)
```
````
