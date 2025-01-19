import unittest
from textnode import * 

class TestInlineMD(unittest.TestCase):
    def test_inline_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.NORMAL)
        newNode = split_nodes_delimiter([node], "**",TextType.BOLD)
        
        self.assertEqual(
            [
                TextNode('This is text with a ', TextType.NORMAL, None),
                TextNode('bolded', TextType.BOLD, None), 
                TextNode(' word', TextType.NORMAL, None)
            ],
            newNode,
        )
        
    def test_inline_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.NORMAL)
        newNode = split_nodes_delimiter([node], "*",TextType.ITALIC)
        
        self.assertEqual(
            [
                TextNode('This is text with a ', TextType.NORMAL, None),
                TextNode('italic', TextType.ITALIC, None), 
                TextNode(' word', TextType.NORMAL, None)
            ],
            newNode,
        )
    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
                TextNode("",TextType.NORMAL)
            ],
            new_nodes,
        )
    

if __name__ == "__main__":
    unittest.main()