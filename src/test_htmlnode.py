import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html1 = HTMLNode("a", "This is me", None, {"href": "google.com", "target": "_blank"})
        compare1 = HTMLNode.props_to_html(html1)
        compare2 = ' href="google.com" target="_blank"'
        self.assertEqual(compare1, compare2)

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf1 = LeafNode("a", "This is me", {"abc": "def"})
        compare1 = LeafNode.to_html(leaf1)
        compare2 = '<a abc="def">This is me</a>'
        self.assertEqual(compare1, compare2)

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        compare1 = ParentNode.to_html(parent_node)
        compare2 = "<div><span><b>grandchild</b></span></div>"
        self.assertEqual(compare1, compare2)

if __name__ == "__main__":
    unittest.main()

