from typing import Tuple, Dict, Optional, Any
# from models.animation import Animation  # Placeholder for future animation support


class Character:
    def __init__(
        self,
        id: str,
        name: str,
        sprite_sheet: str,
        position: Tuple[int, int],
        animations: Optional[Dict[str, Any]] = None,
        dialogue_tree_id: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.sprite_sheet = sprite_sheet
        self.position = position
        self.animations = animations or {}  # keys like "walk", "talk"
        self.dialogue_tree_id = dialogue_tree_id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "sprite_sheet": self.sprite_sheet,
            "position": self.position,
            "animations": self.animations,  # Placeholder for now
            "dialogue_tree_id": self.dialogue_tree_id
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            id=data["id"],
            name=data["name"],
            sprite_sheet=data["sprite_sheet"],
            position=tuple(data["position"]),
            animations=data.get("animations", {}),
            dialogue_tree_id=data.get("dialogue_tree_id")
        )
