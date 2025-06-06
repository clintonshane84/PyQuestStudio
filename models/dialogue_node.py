from typing import List, Dict, Any
from models.dialogue_response import DialogueResponse


class DialogueNode:
    def __init__(self, id: str, text: str, responses: List[DialogueResponse]):
        self.id = id
        self.text = text
        self.responses = responses

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "responses": [r.to_dict() for r in self.responses]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            id=data["id"],
            text=data["text"],
            responses=[DialogueResponse.from_dict(r) for r in data["responses"]]
        )
