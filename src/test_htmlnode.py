import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):

    
    def test_parent_node_creation(self):
        """Test that a ParentNode is created correctly."""
        child1 = LeafNode(value="Hello, world!", tag="p")
        child2 = LeafNode(value="Click me!", tag="a", props={"href": "https://example.com"})

        parent = ParentNode(tag="div", children=[child1, child2], props={"class": "container"})

        self.assertEqual(parent.tag, "div")
        self.assertEqual(parent.props, {"class": "container"})
        self.assertEqual(len(parent.children), 2)

    def test_to_html(self):
        """Test that the to_html method correctly generates HTML."""
        child1 = LeafNode(value="Hello, world!", tag="p")
        child2 = LeafNode(value="Click me!", tag="a", props={"href": "https://example.com"})

        parent = ParentNode(tag="div", children=[child1, child2], props={"class": "container"})

        expected_html = '<div class="container"><p>Hello, world!</p><a href="https://example.com">Click me!</a></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_no_tag(self):
        """Test that ValueError is raised when tag is missing."""
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[LeafNode(value="Child", tag="p")])

    def test_no_children(self):
        """Test that ValueError is raised when children is missing or not a list."""
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=None)

        with self.assertRaises(ValueError):
            ParentNode(tag="div", children="Not a list")

    def test_empty_children(self):
        """Test that ParentNode with empty children is handled correctly."""
        parent = ParentNode(tag="div", children=[], props={"class": "empty-container"})
        expected_html = "<div class=\"empty-container\"></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_nested_parent_node(self):
        """Test handling of nested ParentNodes."""
        nested_child = ParentNode(tag="ul", children=[
            LeafNode(value="Item 1", tag="li"),
            LeafNode(value="Item 2", tag="li")
        ])

        root = ParentNode(tag="div", children=[
            LeafNode(value="Welcome!", tag="h1"),
            nested_child
        ])

        expected_html = '<div><h1>Welcome!</h1><ul><li>Item 1</li><li>Item 2</li></ul></div>'
        self.assertEqual(root.to_html(), expected_html)

    
if __name__ == "__main__":
    unittest.main()