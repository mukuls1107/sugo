from textnode import TextNode

print("hello world")


def main():
    dummy = TextNode("this is a text node", "bold", "https://github.com")
    print(dummy.__repr__())



main()