import json
from typing import Dict, Any
from models.scene import Scene
from models.character import Character
from models.asset_library import AssetLibrary


class GameProject:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.scenes: Dict[str, Scene] = {}
        self.characters: Dict[str, Character] = {}
        self.assets = AssetLibrary()
        self.settings: Dict[str, Any] = {}

    def add_scene(self, scene: Scene):
        self.scenes[scene.id] = scene

    def remove_scene(self, scene_id: str):
        self.scenes.pop(scene_id, None)

    def add_character(self, character: Character):
        self.characters[character.id] = character

    def remove_character(self, character_id: str):
        self.characters.pop(character_id, None)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "description": self.description,
            "scenes": {sid: scene.to_dict() for sid, scene in self.scenes.items()},
            "characters": {cid: char.to_dict() for cid, char in self.characters.items()},
            "assets": self.assets.to_dict(),
            "settings": self.settings,
        }

    def save_to_file(self, file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load_from_file(cls, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        project = cls(data['title'], data.get('description', ""))
        # Scene and Character loading would call from_dict (to be implemented later)
        return project
