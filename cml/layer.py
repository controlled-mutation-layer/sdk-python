import uuid
import datetime
from typing import Any, Callable, Dict, Tuple

from .turn import Turn

DecisionFn = Callable[[Dict[str, Any], Dict[str, Any]], Tuple[str, Dict[str, Any]]]

def execute_turn(
    *,
    pre_state: Dict[str, Any],
    signals: Dict[str, Any],
    policy_version: str,
    decision_fn: DecisionFn,
) -> Turn:
    """
    Wrap a decision boundary and return a Turn.

    decision_fn(pre_state, signals) -> (decision_label, post_state)
    """
    decision_label, post_state = decision_fn(pre_state, signals)

    return Turn(
        turn_id=str(uuid.uuid4()),
        timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        pre_state=pre_state,
        signals=signals,
        policy_version=policy_version,
        decision=decision_label,
        post_state=post_state,
    )
