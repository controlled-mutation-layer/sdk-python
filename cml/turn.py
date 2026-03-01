import uuid
import datetime
import json
from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class Turn:
    turn_id: str
    timestamp: str
    pre_state: Dict[str, Any]
    signals: Dict[str, Any]
    policy_version: str
    decision: str
    post_state: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)