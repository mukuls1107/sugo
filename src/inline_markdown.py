from textnode import LeafNode, TextNode,TextType
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(tag="p", value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b",value= text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i",value= text_node.text)
    if text_node.text_type == TextType.CODE:
        
        return LeafNode(tag="code",value= text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a",value= text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img",value= "", props={"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")


# Split Delimeters 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # if not isinstance(old_nodes, TextType):
    #     print("not a normal text-type")
    #     return old_nodes
    
    # splited =str(old_nodes.text).split(delimiter)
    
    # for i, part in enumerate(splited):
    #     print(i,part)
    
    # print(splited)
    
    if old_nodes[0].text_type != TextType.NORMAL:
        print("Not a Normal TextType")
        return
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(f"Invalid markdown, {text_type} section not closed")
            for i, part in enumerate(parts):
                # Alternate between normal text and the specified text_type for delimited parts
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            # Non-text nodes are added as it iis
            new_nodes.append(node)
            
    return new_nodes
    


# newNode = text_node_to_html_node(node)
# print(newNode)

# sp = split_nodes_delimiter([node], "**",TextType.BOLD)

# node = TextNode(
#             "This is text with a **bolded** word and **another**", TextType.BOLD
#         )
# node = TextNode(
            # "This is text with a **bolded** word and **another**", TextType.NORMAL
        # )# node = TextNode("This is text with a **bolded** word", TextType.NORMAL)

# new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
# print(new_nodes)
# for each in new_nodes:
#     print(each)

def extract_markdown_images(text):
    # r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    all_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return all_images
    
    # print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))

    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]))
    
def extract_markdown_links(text):
    all_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
,text)
    return all_links