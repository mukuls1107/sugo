from enum import Enum
from htmlnode import ParentNode, HTMLNode
from inline_markdown import text_to_textnodes,text_node_to_html_node

class BlockType(Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    QUOTE = "quote"
    O_LIST = "ordered_list"
    U_LIST = "unordered_list"
    CODE = "code"


def markdown_to_blocks(markdown):
    if not markdown:
        return []
        
    lines = markdown.strip().split("\n")
    blocks = []
    current_block = []

    for line in lines:
        if line.strip() == "":
            if current_block:
                block_content = "".join(current_block).strip()
                if block_content:
                    blocks.append(block_content)
                current_block = []
        else:
            current_block.append(line)

    # Handle last block
    if current_block:
        block_content = "".join(current_block).strip()
        if block_content:
            blocks.append(block_content)

    # Additional validation
    filtered_blocks = []
    for block in blocks:
        if block.strip():
            filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return BlockType.HEADING.value
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH.value
        return BlockType.QUOTE.value
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE.value
    
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH.value
        return BlockType.U_LIST.value
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.U_LIST.value
        return BlockType.U_LIST.value
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH.value
            i += 1
        return BlockType.O_LIST.value
    return BlockType.PARAGRAPH.value


# block = """- Normal Unordered list"""

# print(block_to_block_type(block=block))

def markdown_to_html_node(markdown):
    block_of_markdown = markdown_to_blocks(markdown)
    children = []
    for each_block in block_of_markdown:
        html_node = block_to_html_code(each_block)
        children.append(html_node)
    
    return ParentNode("div",children,None)


def block_to_html_code(block):
    type_Of_Block = block_to_block_type(block)
    
    if type_Of_Block == "paragraph":
        return paragraph_to_html_node(block)
    
    if type_Of_Block == "code":
        return code_to_html_node(block)
    
    if type_Of_Block == "heading":
        return heading_to_html_node(block)
    
    if type_Of_Block == "ordered_list":
        return olist_to_html_node(block)
    
    if type_Of_Block == "quote":
        return quote_to_html_node(block)
    
    if type_Of_Block == "unordered_list":
        return ulist_to_html_node(block)
        



def text_to_children(text):
    if not text or not text.strip():
        return []
        
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        if text_node.text and text_node.text.strip():
            html_node = text_node_to_html_node(text_node)
            if html_node:
                children.append(html_node)
    return children


        
def paragraph_to_html_node(block):
    if not block or not block.strip():
        return None
        
    lines = block.split("\n")
    paragraph = " ".join(line.strip() for line in lines if line.strip())
    if not paragraph:
        return None
        
    children = text_to_children(paragraph)
    if not children:
        return None
        
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
    
    
markdown_to_html_node(
"""# Heading 1 
## Heading 2
- Unordered list
> Quote""")