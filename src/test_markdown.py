import unittest
from markdown import markdown_to_blocks

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
