import unittest

from textnode import TextNode, split_nodes_delimiter, text_node_to_html_node, split_nodes_image, split_nodes_link, text_to_textnodes
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_to_html_node(self):
        raw_text = TextNode("Raw Text", "text")
        raw_html = LeafNode("Raw Text")
        self.assertEqual(text_node_to_html_node(raw_text), raw_html)
        link_text = TextNode("Click Here", "link", "www.buxogabriel.vercel.app")
        link_html = LeafNode("Click Here", "a", {"href": "www.buxogabriel.vercel.app"})
        self.assertEqual(text_node_to_html_node(link_text), link_html)
        image_text = TextNode("Alt Text", "image", "127.0.0.1")
        image_html = LeafNode("", "img", {"src": "127.0.0.1", "alt": "Alt Text"})
        self.assertEqual(text_node_to_html_node(image_text), image_html)

    def test_split_nodes_delimiter(self):
        old_node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([old_node], "`", "code")
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", "text")
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", "text"),
            TextNode("second image", "image", "https://i.imgur.com/3elNhQu.png")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://buxogabriel.vercel.app) and another [second link](https://www.github.com/buxogabriel)", "text")
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("link", "link", "https://buxogabriel.vercel.app"),
            TextNode(" and another ", "text"),
            TextNode("second link", "link", "https://www.github.com/buxogabriel")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev")
        ]
        self.assertEqual(nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()
