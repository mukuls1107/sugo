import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a note equal text node", TextType.BOLD)
        node2 = TextNode("This is a note equal text node", TextType.ITALIC)
        self.assertNotEqual(node,node2)
    
    def test_urls(self):
        node = TextNode("This check the URL", TextType.LINK)
        node2 = TextNode("This check the URL", TextType.LINK)
        self.assertEqual(node, node2)
        
    
if __name__ == "__main__":
    unittest.main()