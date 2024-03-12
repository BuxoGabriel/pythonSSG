import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        empty = HTMLNode()
        empty_repr = "HTMLNode(None, None, None, None)"
        self.assertEqual(empty.__repr__(), empty_repr)
        props = {
            "prop1": "val1",
            "prop2": "val2"
        }
        value_tag = HTMLNode(tag="a", props=props, value="val")
        value_repr = "HTMLNode(a, val, {'prop1': 'val1', 'prop2': 'val2'}, None)"
        self.assertEqual(value_tag.__repr__(), value_repr)
        children_tag = HTMLNode(tag="a", props=props, children=[empty])
        children_repr = "HTMLNode(a, None, {'prop1': 'val1', 'prop2': 'val2'}, [HTMLNode(None, None, None, None)])"
        self.assertEqual(children_tag.__repr__(), children_repr)

    def test_to_html(self):
        empty = HTMLNode()
        self.assertRaises(NotImplementedError, empty.to_html)

if __name__ == "__main__":
    unittest.main()
