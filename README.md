# Controlled Mutation Layer (CML) — Python SDK

Current stable preview: **v0.1.4**

The Controlled Mutation Layer (CML) Python SDK provides a minimal, structured representation of mutation events at the decision boundary.

It allows systems to emit deterministic, inspectable `Turn` records whenever authoritative state changes.

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

CML instruments the mutation boundary so every consequential change becomes explicit.

---

## Atomic Unit: `Turn`

A `Turn` captures:

- `turn_id` — unique mutation identifier
- `timestamp` — UTC ISO8601 string
- `pre_state` — state before mutation
- `signals` — bounded metadata describing context
- `policy_version` — governing policy version
- `decision` — structured decision label
- `post_state` — state after mutation

If you can’t answer “Why did this change?”, you don’t have a Turn.

---

## Install

### From GitHub (recommended)

```bash
pip install --no-cache-dir "cml @ git+https://github.com/controlled-mutation-layer/sdk-python.git@v0.1.4"
```

Verify installation:

```bash
python -c "import importlib.metadata as m; print(m.version('cml'))"
```

---

### For Contributors (Editable Install)

```bash
git clone https://github.com/controlled-mutation-layer/sdk-python.git
cd sdk-python
python -m venv .venv
source .venv/bin/activate
pip install -e .
pytest -q
```

---

## First Run (2 minutes)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --no-cache-dir "cml @ git+https://github.com/controlled-mutation-layer/sdk-python.git@v0.1.4"
```

```python
import datetime
from uuid import uuid4
from cml import Turn

turn = Turn(
    turn_id=str(uuid4()),
    timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    pre_state={"refund_policy": "v1", "max_refund": 50},
    signals={
        "entity": "refund_policy",
        "actor": "dev:first_run",
        "reason_codes": ["policy_update"],
    },
    policy_version="v0",
    decision="update_refund_policy",
    post_state={"refund_policy": "v2", "max_refund": 75},
)

print(turn.to_json())
```

---

## Quickstart

`pre_state` and `post_state` describe what changed.  
`signals` carries bounded metadata (actor, reason codes, correlation ids, etc.) describing why and how the mutation occurred.

Wrap a state mutation so every commit emits a structured `Turn` record.

```python
import datetime
from uuid import uuid4
from cml import Turn

pre_state = {"refund_policy": "v1", "max_refund": 50}
post_state = {"refund_policy": "v2", "max_refund": 75}

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

print(turn.to_dict())
print(turn.to_json())
```

---

## Examples

Run:

```bash
python examples/refund_drift_demo.py
```

---

## Specification

For the conceptual model and formal definition of the mutation boundary, see:

https://github.com/controlled-mutation-layer/cml-spec
