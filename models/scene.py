from typing import List, Dict
from models.interactive_object import InteractiveObject
from models.polygon import Polygon


class Scene:
    def __init__(self, id: str, name: str, background_image: str):
        self.id = id
        self.name = name
        self.background_image = background_image
        self.objects: List[InteractiveObject] = []
        self.characters: List[str] = []
        self.no_go_zones: List[Polygon] = []
        self.exit_points: Dict[str, str] = {}

    def add_object(self, obj: InteractiveObject):
        self.objects.append(obj)

    def add_character(self, character_id: str):
        if character_id not in self.characters:
            self.characters.append(character_id)

    def add_exit_point(self, trigger: str, target_scene_id: str):
        self.exit_points[trigger] = target_scene_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "background_image": self.background_image,
            "objects": [obj.to_dict() for obj in self.objects],
            "characters": self.characters,
            "no_go_zones": [zone.to_dict() for zone in self.no_go_zones],
            "exit_points": self.exit_points,
        }

    @classmethod
    def from_dict(cls, data: Dict):
        scene = cls(data["id"], data["name"], data["background_image"])
        # Load objects and zones from sub-dictionaries
        # These will be implemented in InteractiveObject and Polygon
        return scene
