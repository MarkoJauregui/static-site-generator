import unittest
from textnode import TextNode, TextType
from node_splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link


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


class TestSplitNodesImageAndLink(unittest.TestCase):

    def test_split_nodes_link(self):
        node = TextNode(
            "Check this [link1](http://example.com) and [link2](http://another.com)",
            TextType.TEXT,
        )
        expected = [
            TextNode("Check this ", TextType.TEXT),
            TextNode("link1", TextType.LINK, "http://example.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "http://another.com"),
        ]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

    def test_single_link(self):
        node = TextNode("Visit [Boot.dev](https://www.boot.dev)", TextType.TEXT)
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
        ]
        result = split_nodes_link([node])
        self.assertEqual(expected, result)

    def test_multiple_links(self):
        node = TextNode(
            "Visit [Boot.dev](https://www.boot.dev) and [Youtube](https://www.youtube.com)",
            TextType.TEXT,
        )
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Youtube", TextType.LINK, "https://www.youtube.com"),
        ]
        result = split_nodes_link([node])
        self.assertEqual(expected, result)

    def test_no_link(self):
        node = TextNode("Don't go to boot.dev", TextType.TEXT)
        expected = [TextNode("Don't go to boot.dev", TextType.TEXT)]
        result = split_nodes_link([node])
        self.assertEqual(expected, result)

    def test_split_images(self):
        node = TextNode(
            "Here is an image: ![Alt text](https://example.com/image.jpg) and more text.",
            TextType.TEXT,
        )
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("Alt text", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(" and more text.", TextType.TEXT),
        ]
        result = split_nodes_image([node])
        self.assertEqual(expected, result)

    def test_single_image(self):
        node = TextNode(
            "Here is an image: ![Alt text](https://example.com/image.jpg)",
            TextType.TEXT,
        )
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("Alt text", TextType.IMAGE, "https://example.com/image.jpg"),
        ]
        result = split_nodes_image([node])
        self.assertEqual(expected, result)

    def test_multiple_images(self):
        node = TextNode(
            "Here is an image: ![Alt text](https://example.com/image.jpg) and another image ![Second Alt Text](https://example.com/image2.jpg)",
            TextType.TEXT,
        )
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("Alt text", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(" and another image ", TextType.TEXT),
            TextNode(
                "Second Alt Text", TextType.IMAGE, "https://example.com/image2.jpg"
            ),
        ]
        result = split_nodes_image([node])
        self.assertEqual(expected, result)

    def test_no_image(self):
        node = TextNode("Here is no image", TextType.TEXT)
        expected = [TextNode("Here is no image", TextType.TEXT)]
        result = split_nodes_image([node])
        self.assertEqual(expected, result)

    def test_wrong_link(self):
        node = TextNode("Here is a useless link [Boot.dev]", TextType.TEXT)
        expected = [TextNode("Here is a useless link [Boot.dev]", TextType.TEXT)]
        result = split_nodes_link([node])
        self.assertEqual(expected, result)

    def test_wrong_image(self):
        node = TextNode(
            "Here is a bad image (https://example.com/image.jpg)", TextType.TEXT
        )
        expected = [
            TextNode(
                "Here is a bad image (https://example.com/image.jpg)", TextType.TEXT
            )
        ]
        result = split_nodes_image([node])
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
