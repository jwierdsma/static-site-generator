import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("click here", TextType.LINK, "https://example.com")
        node2 = TextNode("click here", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)
 
    def test_not_eq_different_text(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("world", TextType.BOLD)
        self.assertNotEqual(node, node2)
 
    def test_not_eq_different_type(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node, node2)
 
    def test_not_eq_different_url(self):
        node = TextNode("click", TextType.LINK, "https://a.com")
        node2 = TextNode("click", TextType.LINK, "https://b.com")
        self.assertNotEqual(node, node2)
 
    def test_url_defaults_to_none(self):
        node = TextNode("hello", TextType.TEXT)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
