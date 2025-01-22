# src/textnode.py
from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, TEXT, TYPE,URL=None):
        self.text = TEXT
        self.text_type = TextType(TYPE)
        self.url = URL
        
    def __eq__(self, other):
        if not isinstance(other, TextNode):
                return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
            )
        
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type.value}, {self.url!r})"

