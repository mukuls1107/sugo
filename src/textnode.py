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

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")

