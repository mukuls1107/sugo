from textnode import TextNode, TextType
from htmlnode import LeafNode
print("hello world")


def main():
    dummy = TextNode("this is a text node", "bold", "https://github.com")
    
    if dummy.text_type.value == "bold":
        print(dummy.text)
        print("It is bold")
    # print(dummy.__repr__())

# def text_node_to_html_node(textNode):
#     match textNode.text_type.value:
#         case "normal":
#             return LeafNode(value=textNode.text)
        
#         case "bold":
#             return LeafNode(value=textNode.text, tag="b")
#         case "italic":
#             return LeafNode(value=textNode.text, tag="i")
#         case "code":
#             return LeafNode(value=textNode.text, tag="code")
#         case "link":
#             return LeafNode(value=textNode.text, tag="a",props={"href":textNode.props["href"]})
#         case "img":
#             return LeafNode(tag="img", value="", props={"src": textNode.props["src"], "alt": textNode.props["alt"]})
        
#         case _:
#             return 


  