from typing import Dict, Any
from models.dialogue_node import DialogueNode


class DialogueTree:
    def __init__(self, id: str, start_node_id: str):
        self.id = id
        self.start_node_id = start_node_id
        self.nodes: Dict[str, DialogueNode] = {}

    def add_node(self, node: DialogueNode):
        self.nodes[node.id] = node

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "start_node_id": self.start_node_id,
            "nodes": {nid: node.to_dict() for nid, node in self.nodes.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        tree = cls(id=data["id"], start_node_id=data["start_node_id"])
        for nid, ndata in data["nodes"].items():
            tree.add_node(DialogueNode.from_dict(ndata))
        return tree
