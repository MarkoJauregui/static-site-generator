import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_basic_parent(self):
        child = LeafNode("b", "Bold text")
        parent = ParentNode("p", [child])
        self.assertEqual(parent.to_html(), "<p><b>Bold text</b></p>")

    def testMultipleChildren(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
        ]
        parent = ParentNode("p", children)
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i></p>"
        self.assertEqual(parent.to_html(), expected)

    def testWithNoTag(self):
        child = LeafNode("b", "Bold text")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def testWithNoChild(self):
        parent = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def testParentOfParent(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
        ]
        parent = ParentNode("p", children)
        grandparent = ParentNode("p", [parent])
        expected = "<p><p><b>Bold text</b>Normal text<i>italic text</i></p></p>"
        self.assertEqual(grandparent.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
