from typing import Optional, Dict, Any


class DialogueResponse:
    def __init__(self, text: str, next_node_id: Optional[str], trigger_event: Optional[Dict[str, Any]] = None):
        self.text = text
        self.next_node_id = next_node_id
        self.trigger_event = trigger_event or {}

    def to_dict(self):
        return {
            "text": self.text,
            "next_node_id": self.next_node_id,
            "trigger_event": self.trigger_event
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            text=data["text"],
            next_node_id=data.get("next_node_id"),
            trigger_event=data.get("trigger_event", {})
        )
