import json
import random
import sys
from pathlib import Path
from statistics import mean

if __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from cml.layer import execute_turn

random.seed(42)


def refund_policy_factory(threshold):
    def refund_policy(pre_state, signals):
        if signals["amount"] < threshold:
            decision = "approve_refund"
            post_state = {**pre_state, "refund_status": "approved"}
        else:
            decision = "manual_review"
            post_state = {**pre_state, "refund_status": "pending_review"}
        return decision, post_state

    return refund_policy


def simulate(days=90):
    turns = []

    for day in range(days):
        # Policy change at midpoint.
        if day < days // 2:
            threshold = 50
            policy_version = "refund_v1"
        else:
            threshold = 30
            policy_version = "refund_v2"

        policy = refund_policy_factory(threshold)

        turn = execute_turn(
            pre_state={"refund_status": "none"},
            signals={"amount": random.randint(1, 100)},
            policy_version=policy_version,
            decision_fn=policy,
        )
        turns.append(turn)

    return turns


def approval_rate(turns):
    return mean(t.decision == "approve_refund" for t in turns)


if __name__ == "__main__":
    turns = simulate()

    first_half = turns[: len(turns)//2]
    second_half = turns[len(turns)//2 :]

    rate_before = approval_rate(first_half)
    rate_after = approval_rate(second_half)

    print("\n--- Refund Drift Demo ---\n")
    print(f"Approval rate before change: {rate_before:.2f}")
    print(f"Approval rate after change:  {rate_after:.2f}")

    out_path = Path("data/turns.jsonl")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for t in turns:
            f.write(json.dumps(t.to_dict()) + "\n")
    print(f"\nWrote {len(turns)} Turns to: {out_path}")

    policy_versions = {t.policy_version for t in turns}
    if len(policy_versions) > 1:
        print("\nRoot cause: policy_version change detected.")
    else:
        print("\nPolicy stable. Behavior shift likely due to signal distribution change.")
