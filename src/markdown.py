from parentnode import ParentNode
from textnode import text_node_to_html_node, text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown: str):
    return list(map(lambda block: block.lstrip().rstrip(), markdown.split("\n\n")))

def block_to_block_type(block: str):
    block = block.strip()
    # Check if ends match code block
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    # Check if header
    header_level = 0
    for char in block:
        if char == "#":
            header_level += 1
        else:
            break
    if header_level != 0:
        if header_level > 6:
            return block_type_paragraph
        return f"{block_type_heading}_{header_level}"

    # check if every line matches a pattern
    lines = block.splitlines()
    block_type = get_block_from_line_start(block, 1)

    for line_index in range(len(lines)):
        line = lines[line_index]
        if get_block_from_line_start(line, line_index + 1) != block_type:
            return block_type_paragraph
    return block_type

# Helper for determining block type
def get_block_from_line_start(line: str, line_num: int):
    if line.startswith(">"):
        return block_type_quote
    elif line.startswith("- ") or line.startswith("* "):
        return block_type_unordered_list
    elif line.startswith(f"{line_num}. "):
        return block_type_ordered_list
    else:
        return block_type_paragraph

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(block_to_html_node(block, block_type))
    return ParentNode("div", children)

def block_to_html_node(block: str, block_type: str):
    if block_type == block_type_paragraph:
        return paragraph_to_htmlnode(block)
    elif block_type == block_type_code:
        return code_to_htmlnode(block)
    elif block_type == block_type_quote:
        return quote_to_htmlnode(block)
    elif block_type.startswith(block_type_heading):
        heading_level = int(block_type[len(block_type_heading) + 1])
        return heading_to_htmlnode(block, heading_level)
    elif block_type == block_type_unordered_list:
        return unordered_to_htmlnode(block)
    elif block_type == block_type_ordered_list:
        return ordered_to_htmlnode(block)

## HELPERS
# Helpers for turning specific blocks into specific html parent nodes

def paragraph_to_htmlnode(block: str):
    text_nodes = text_to_textnodes(block)
    if len(text_nodes) == 1 and text_nodes[0].text_type != None:
        return text_node_to_html_node(text_nodes[0])
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    return ParentNode("p", html_nodes)

def code_to_htmlnode(block: str):
    text_nodes = text_to_textnodes(block[3:-3])
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    return ParentNode("pre", [ParentNode("code", html_nodes)])

def quote_to_htmlnode(block: str):
    lines = block.splitlines(True)
    text_nodes = [text_node for line in lines for text_node in text_to_textnodes(line[1:])]
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    return ParentNode("blockquote", html_nodes)

def heading_to_htmlnode(block: str, heading_level: int):
    text = block.lstrip("# ")
    text_nodes = text_to_textnodes(text)
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    return ParentNode(f"h{heading_level}", html_nodes)

def unordered_to_htmlnode(block: str):
    lines = block.splitlines()
    list_items = []
    for line in lines:
        text_nodes = text_to_textnodes(line)
        html_nodes = list(map(text_node_to_html_node, text_nodes))
        list_items.append(ParentNode("li", html_nodes))
    return ParentNode("ul", list_items)

def ordered_to_htmlnode(block: str):
    lines = block.splitlines()
    list_items = []
    for line in lines:
        text_nodes = text_to_textnodes(line)
        html_nodes = list(map(text_node_to_html_node, text_nodes))
        list_items.append(ParentNode("li", html_nodes))
    return ParentNode("ol", list_items)

def extract_title(markdown: str):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception
