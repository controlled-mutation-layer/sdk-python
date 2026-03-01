import json
from collections import defaultdict
from pathlib import Path

TURNS_PATH = Path("data/turns.jsonl")

def load_turns(path: Path):
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)

if __name__ == "__main__":
    if not TURNS_PATH.exists():
        raise SystemExit(f"Missing {TURNS_PATH}. Run: python examples/refund_drift_demo.py")

    counts_by_policy = defaultdict(int)
    approvals_by_policy = defaultdict(int)

    total = 0
    for t in load_turns(TURNS_PATH):
        total += 1
        pv = t["policy_version"]
        counts_by_policy[pv] += 1
        if t["decision"] == "approve_refund":
            approvals_by_policy[pv] += 1

    print(f"\nLoaded {total} Turns from {TURNS_PATH}\n")
    print("Policy version summary (like GROUP BY policy_version):")
    for pv in sorted(counts_by_policy.keys()):
        n = counts_by_policy[pv]
        approvals = approvals_by_policy[pv]
        rate = approvals / n if n else 0.0
        print(f"  {pv}: count={n}, approvals={approvals}, approval_rate={rate:.2f}")
