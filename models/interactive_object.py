from typing import Tuple, Dict, Any


class InteractiveObject:
    def __init__(
        self,
        id: str,
        name: str,
        sprite: str,
        position: Tuple[int, int],
        interaction_type: str,
        metadata: Dict[str, Any] = None
    ):
        self.id = id
        self.name = name
        self.sprite = sprite
        self.position = position
        self.interaction_type = interaction_type  # e.g., "dialogue", "scene_transition", "item"
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "sprite": self.sprite,
            "position": self.position,
            "interaction_type": self.interaction_type,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            id=data["id"],
            name=data["name"],
            sprite=data["sprite"],
            position=tuple(data["position"]),
            interaction_type=data["interaction_type"],
            metadata=data.get("metadata", {})
        )
