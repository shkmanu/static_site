import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html1 = HTMLNode(None, None, None, {"a": "123", "b": "456"})
        compare1 = HTMLNode.props_to_html(html1)
        compare2 = f'a="123" b="456"'
        self.assertEqual(compare1, compare2)

if __name__ == "__main__":
    unittest.main()

