from textnode import *
from htmlnode import *

def main():

    Example = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    Example2 = HTMLNode("h1", "hello", None, {"a": "123", "b": "456"})
    print(Example2)

main()
