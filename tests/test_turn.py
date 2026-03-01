from cml.layer import execute_turn


def dummy_policy(pre_state, signals):
    return "approve", {**pre_state, "refund_status": "approved"}


def test_turn_structure():
    turn = execute_turn(
        pre_state={"refund_status": "none"},
        signals={"amount": 50},
        policy_version="v1",
        decision_fn=dummy_policy,
    )

    data = turn.to_dict()

    assert data["policy_version"] == "v1"
    assert data["decision"] == "approve"
    assert data["pre_state"]["refund_status"] == "none"
