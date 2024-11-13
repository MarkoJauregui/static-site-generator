from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node
import unittest


class TestTextToHtml(unittest.TestCase):
    def test_text_node_conversion(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {})

    def test_text_node_bold_conversion(self):
        text_node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.props, {})

    def test_text_node_italic_conversion(self):
        text_node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        self.assertEqual(html_node.props, {})

    def test_text_node_code_conversion(self):
        text_node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.props, {})

    def test_text_node_link_conversion(self):
        text_node = TextNode(
            "This is a link node", TextType.LINK, "https://www.boot.dev"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_text_node_image_conversion(self):
        text_node = TextNode(
            "This is an image node", TextType.IMAGE, "https://image.url/pic.jpg"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://image.url/pic.jpg", "alt": "This is an image node"},
        )


if __name__ == "__main__":
    unittest.main()
