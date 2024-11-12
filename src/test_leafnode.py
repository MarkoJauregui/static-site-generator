import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_basic_leaf_node(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")
    
    def test_leaf_node_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_none_value(self):
        node = LeafNode("p", None) 
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_none_tag(self):
        node = LeafNode(None, "Just some raw text")
        self.assertEqual(node.to_html(), "Just some raw text")
    
    def test_empty_props(self):
        node = LeafNode("p", "text", {})
        self.assertEqual(node.to_html(), "<p>text</p>")

if __name__ == '__main__':
    unittest.main()