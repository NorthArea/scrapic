import unittest
from scrapic import Item


class ItemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.val = 'val'

    def test_main(self):
        item = Item(self.val)
        self.assertEqual(self.val, item.val())

    def test_is_alive(self):
        item = Item(self.val)
        self.assertTrue(item.is_alive())
        item.destroy()
        self.assertFalse(item.is_alive())

    def test_ttl(self):
        item = Item(self.val, 5)
        self.assertTrue(item.is_alive())
        item._create_timestamp -= 20
        self.assertFalse(item.is_alive())
