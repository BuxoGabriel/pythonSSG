from leafnode import LeafNode
from regex import extract_markdown_links, extract_markdown_images

text_types = {
    "text": None,
    "bold": "b",
    "italic": "i",
    "code": "code",
}

class TextNode:
    def __init__(self, text: str, text_type: str, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, TextNode):
            return False
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case "image":
            props = {}
            props["alt"] = text_node.text
            props["src"] = text_node.url
            return LeafNode("", "img", props)
        case "link":
            props = {}
            props["href"] = text_node.url
            return LeafNode(text_node.text, "a", props)
        case _:
            if text_node.text_type not in text_types:
                raise ValueError(f"Invalid text type {text_node.text_type}")
            return LeafNode(text_node.text, text_types[text_node.text_type], None)

def split_nodes_delimiter(old_nodes, delimiter: str, text_type: str):
    new_nodes = []
    for node in old_nodes:
        split_node = node.text.split(delimiter)
        outside = True
        for part in split_node:
            text_node_type = text_type
            if outside:
                text_node_type = node.text_type
            new_nodes.append(TextNode(part, text_node_type, node.url))
            outside = not outside
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        node_text = node.text
        for (name, src) in images:
            split_node = node_text.split(f"![{name}]({src})", 1)
            if(split_node[0] != ""):
                new_nodes.append(TextNode(split_node[0], node.text_type, node.url))
            new_nodes.append(TextNode(name, "image", src))
            node_text = split_node[1]
        if(node_text != ""):
            new_nodes.append(TextNode(node_text, node.text_type, node.url))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        node_text = node.text
        for (text, src) in links:
            split_node = node_text.split(f"[{text}]({src})", 1)
            if(split_node[0] != ""):
                new_nodes.append(TextNode(split_node[0], node.text_type, node.url))
            new_nodes.append(TextNode(text, "link", src))
            node_text = split_node[1]
        if(node_text != ""):
            new_nodes.append(TextNode(node_text, node.text_type, node.url))
    return new_nodes

def text_to_textnodes(text: str):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    return nodes
