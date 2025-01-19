import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","This is a paragraph node", props={"id":"main"}, children=None)
        node2 = HTMLNode("p","This is a paragraph node", props={"id":"main"}, children=None)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("p  ","This is a note equal text node",)
        node2 = HTMLNode("This is a note equal text node", )
        self.assertNotEqual(node,node2)
    
    def test_urls(self):
        node = HTMLNode("a","This check the URL",props={"href":"https://github.com"} )
        node2 = HTMLNode("a","This check the URL",props={"href":"https://github.com"} )
        self.assertEqual(node, node2)
        


class TestLeafNode(unittest.TestCase):
    def test_leafnode_creation(self):
        """Test that LeafNode is created correctly."""
        leaf = LeafNode(value="Image description", tag="img", props={"src": "image.png"})
        self.assertEqual(leaf.tag, "img")
        self.assertEqual(leaf.value, "Image description")
        self.assertEqual(leaf.props["src"], "image.png")
        self.assertEqual(leaf.children, [])

    def test_leafnode_no_children(self):
        """Test that LeafNode does not allow children."""
        leaf = LeafNode(value="Image description", tag="img")
        with self.assertRaises(AttributeError):
            leaf.add_child(None)

    def test_leafnode_empty_value(self):
        """Test that LeafNode requires a non-empty value."""
        with self.assertRaises(ValueError):
            LeafNode(value="", tag="span")


    
if __name__ == "__main__":
    unittest.main()