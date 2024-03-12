import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        invalid = LeafNode(value=None, tag="a", props={})
        self.assertRaises(ValueError, invalid.to_html)
        no_tag = LeafNode(tag=None, value="Raw text")
        no_tag_html = "Raw text"
        self.assertEqual(no_tag.to_html(), no_tag_html)
        no_props = LeafNode(tag="p", value="Paragraph text", props=None)
        no_props_html = "<p>Paragraph text</p>"
        self.assertEqual(no_props.to_html(), no_props_html)
        with_props = LeafNode(tag="a", value="link text", props={"href": "www.website.com"})
        with_props_html = "<a href=\"www.website.com\">link text</a>"
        self.assertEqual(with_props.to_html(), with_props_html)
