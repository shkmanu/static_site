from htmlnode import *
from textnode import *

def text_node_to_html_node(text_node):
    node_text = text_node.text
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, node_text)
        case TextType.BOLD:
            return LeafNode("b", node_text)
        case TextType.ITALIC:
            return LeafNode("i", node_text)
        case TextType.CODE:
            return LeafNode("code", node_text)
        case TextType.LINK:
            return LeafNode("a", node_text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": node_text})
        case _:
            raise Exception("incorrect format")
        

