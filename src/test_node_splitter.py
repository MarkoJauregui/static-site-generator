import unittest
from textnode import TextNode, TextType
from node_splitter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_bold_split(self):
        node = TextNode("Hello, **world**!", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiters(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [TextNode("Just plain text", TextType.TEXT)])

    def test_multiple_delimiters(self):
        node = TextNode("This is **bold** and also **strong** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and also ", TextType.TEXT),
            TextNode("strong", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiters(self):
        node = TextNode("This is **bold without closing", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
