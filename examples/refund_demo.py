from cml.layer import execute_turn

def refund_policy(pre_state, signals):
    # tiny toy policy: approve refunds under $50, otherwise manual review
    if signals["amount"] < 50:
        decision = "approve_refund"
        post_state = {**pre_state, "refund_status": "approved"}
    else:
        decision = "manual_review"
        post_state = {**pre_state, "refund_status": "pending_review"}
    return decision, post_state

if __name__ == "__main__":
    pre_state = {"refund_status": "none"}
    signals = {"amount": 42, "customer_tier": "standard"}

    turn = execute_turn(
        pre_state=pre_state,
        signals=signals,
        policy_version="refund_v1",
        decision_fn=refund_policy,
    )

    print(turn.to_json())
