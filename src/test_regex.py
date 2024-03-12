import unittest

from regex import extract_markdown_images, extract_markdown_links

class TestRegexParsing(unittest.TestCase):
    def test_extract_markdown_images(self):
        markdown = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        expected_extract = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        self.assertEqual(extract_markdown_images(markdown), expected_extract)

    def test_extract_markdown_links(self):
        markdown = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected_extract = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(extract_markdown_links(markdown), expected_extract)
