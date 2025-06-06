from typing import List, Tuple, Dict, Any


class Animation:
    def __init__(self, name: str, frame_rects: List[Tuple[int, int, int, int]], frame_duration: float):
        self.name = name
        self.frame_rects = frame_rects  # List of frame positions on the sprite sheet
        self.frame_duration = frame_duration  # Duration of each frame in seconds

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "frame_rects": self.frame_rects,
            "frame_duration": self.frame_duration
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            name=data["name"],
            frame_rects=[tuple(rect) for rect in data["frame_rects"]],
            frame_duration=data["frame_duration"]
        )
