import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            tag="a", value="Click Here", props={"href": "https://www.example.com"}
        )
        self.assertEqual(
            str(node),
            "HTMLNode(a, Click Here, None, {'href': 'https://www.example.com'})",
        )

    def test_props_to_html(self):
        node = HTMLNode(
            tag="a", value="Click Here", props={"href": "https://www.example.com"}
        )
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com"')


if __name__ == "__main__":
    unittest.main()
