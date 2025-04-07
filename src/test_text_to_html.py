import unittest

from textnode import *
from htmlnode import *
from text_html import *


class TestBOLDHtmlNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        converted = text_node_to_html_node(node1)
        node2 = LeafNode("b", "This is a text node", None)
        self.assertEqual(LeafNode.to_html(converted), LeafNode.to_html(node2))

class TestLINKHtmlNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.LINK, "google.com")
        converted = text_node_to_html_node(node1)
        node2 = LeafNode("a", "This is a text node", {"href": "google.com"})
        self.assertEqual(LeafNode.to_html(converted), LeafNode.to_html(node2))

if __name__ == "__main__":
    unittest.main()