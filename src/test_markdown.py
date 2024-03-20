import unittest
from parentnode import ParentNode
from leafnode import LeafNode
from markdown import block_to_block_type, block_to_html_node, heading_to_htmlnode, markdown_to_blocks, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list, block_type_paragraph

class TestMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = "# this is a heading\n\nAnd here is a **bolded**\nand *italisized* paragraph\n\n\n\n\n\n* list item 1\n* list item 2"""
        block_markdown = markdown_to_blocks(md)
        expected_blocks = [
            "# this is a heading\n",
            "And here is a **bolded**\nand *italisized* paragraph\n",
            "* list item 1\n* list item 2"
        ]
        self.assertEqual(block_markdown, expected_blocks)

    def test_blocktype_code(self):
        md = "```js\nconsole.log(\"hello world\");\n```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_code)

    def test_blocktype_headers(self):
        header_text = "This is a header\nAnd I guess this is part of it too?"
        for i in range(1, 7):
            header_md = ("#" * i) + header_text
            header_type = "heading_" + str(i)
            self.assertEqual(header_type, block_to_block_type(header_md))

    def test_blocktype_quote(self):
        quote_md = ">Life is like riding a bicycle,\n>To keep your balance,\n>You must keep moving"
        self.assertEqual(block_type_quote, block_to_block_type(quote_md))

    def test_blocktype_unordered_list(self):
        unordered_md = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_type_unordered_list, block_to_block_type(unordered_md))
        unordered_md = "* Item 1\n* Item 2\n* Item 3"
        self.assertEqual(block_type_unordered_list, block_to_block_type(unordered_md))

    def test_blocktype_ordered_list(self):
        ordered_md = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_type_ordered_list, block_to_block_type(ordered_md))

    def test_blocktype_paragraph(self):
        paragraph_md = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
        self.assertEqual(block_type_paragraph, block_to_block_type(paragraph_md))

        # Test headers above 6 return paragraph
        paragraph_md = "####### paragraph"
        self.assertEqual(block_type_paragraph, block_to_block_type(paragraph_md))

    def test_heading_to_html_node(self):
        heading_block = "# Heading 1"
        expected_html = ParentNode(tag="h1", children=[LeafNode(tag=None, value="Heading 1")])
        heading_html = heading_to_htmlnode(heading_block, 1)
        self.assertEqual(heading_html, expected_html)
        heading_block = "### Heading 3"
        expected_html = ParentNode(tag="h3", children=[LeafNode(tag=None, value="Heading 3")])
        heading_html = heading_to_htmlnode(heading_block, 3)
        self.assertEqual(heading_html, expected_html)
        
    def test_block_to_html_node(self):
        raise NotImplementedError

    def test_markdown_to_html(self):
        raise NotImplementedError
