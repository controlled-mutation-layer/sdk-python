import random
from statistics import mean
from cml.layer import execute_turn


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
        # Policy change at midpoint
        if day < days // 2:
            threshold = 50
            policy_version = "refund_v1"
        else:
            threshold = 30
            policy_version = "refund_v2"

        policy = refund_policy_factory(threshold)

        pre_state = {"refund_status": "none"}
        signals = {"amount": random.randint(1, 100)}

        turn = execute_turn(
            pre_state=pre_state,
            signals=signals,
            policy_version=policy_version,
            decision_fn=policy,
        )

        turns.append(turn)

    return turns


if __name__ == "__main__":
    turns = simulate()

    first_half = turns[: len(turns)//2]
    second_half = turns[len(turns)//2 :]

    def approval_rate(turns):
        return mean(1 if t.decision == "approve_refund" else 0 for t in turns)

    rate_before = approval_rate(first_half)
    rate_after = approval_rate(second_half)

    print("\n--- Refund Drift Demo ---\n")
    print(f"Approval rate before change: {rate_before:.2f}")
    print(f"Approval rate after change:  {rate_after:.2f}")
    print("\nRoot cause: policy_version changed from refund_v1 to refund_v2")
