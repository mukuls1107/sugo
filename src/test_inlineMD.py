import unittest
from inline_markdown import *

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
    
    def test_extracting_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected)

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        
        self.assertEqual(result,expected)
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another link", TextType.LINK,
                         "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.NORMAL),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()