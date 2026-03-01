# sdk-python# CML Python SDK

### Why did this change?

Modern systems mutate authoritative state.

When behavior changes, engineers ask:

- Was it model drift?
- Policy drift?
- Threshold change?
- Signal shift?
- Human override?

Most systems can’t answer in one query.

The CML Python SDK wraps your decision boundary so every mutation is recorded as a structured Turn.

---

## What This SDK Does

- Captures pre-state
- Records evaluated signals
- Binds mutation to policy version
- Logs authorized mutation
- Enables replay under alternate policy

This is not logging.

This is mutation instrumentation.

---

## Status

Early prototype. Refunds demo coming first.

Contributions welcome.
