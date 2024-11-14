import unittest
from src.text_extraction import extract_markdown_links, extract_markdown_images


class TestTextExtraction(unittest.TestCase):
    def test_basic_image_extraction(self):
        text = "This is an image ![test image](test.jpg)"
        expected = [("test image", "test.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_basic_link_extraction(self):
        text = "This is a link [Boot.dev](https://boot.dev)"
        expected = [("Boot.dev", "https://boot.dev")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_multiple_images(self):
        text = "Here are two images ![first](img1.jpg) and ![second](img2.jpg)"
        expected = [("first", "img1.jpg"), ("second", "img2.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_multiple_links(self):
        text = "Here are two links [first](https://first.com) and [second](https://second.com)"
        expected = [("first", "https://first.com"), ("second", "https://second.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_no_images(self):
        text = "This is text with no images"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_no_links(self):
        text = "This is text with no links"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)
