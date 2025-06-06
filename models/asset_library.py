from typing import Dict, Any


class AssetLibrary:
    def __init__(self):
        self.images: Dict[str, str] = {}     # Backgrounds, icons
        self.sprites: Dict[str, str] = {}    # Sprite sheets
        self.sounds: Dict[str, str] = {}     # Sound effects
        self.music: Dict[str, str] = {}      # Background music

    def add_image(self, asset_id: str, file_path: str):
        self.images[asset_id] = file_path

    def add_sprite(self, asset_id: str, file_path: str):
        self.sprites[asset_id] = file_path

    def add_sound(self, asset_id: str, file_path: str):
        self.sounds[asset_id] = file_path

    def add_music(self, asset_id: str, file_path: str):
        self.music[asset_id] = file_path

    def to_dict(self) -> Dict[str, Any]:
        return {
            "images": self.images,
            "sprites": self.sprites,
            "sounds": self.sounds,
            "music": self.music
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        lib = cls()
        lib.images = data.get("images", {})
        lib.sprites = data.get("sprites", {})
        lib.sounds = data.get("sounds", {})
        lib.music = data.get("music", {})
        return lib
