from textnode import TextNode, TextType
from htmlnode import LeafNode
from copy_static import copy_files_recursive
from generate_content import generate_pages_recursive
import os
import shutil



dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_pages_recursive
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)



    # dummy = TextNode("this is a text node", "bold", "https://github.com")
    
    # if dummy.text_type.value == "bold":
    #     print(dummy.text)
    #     print("It is bold")
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


  
main()