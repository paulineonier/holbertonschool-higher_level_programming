import unittest
from task_02_logic import app

class TestItemsRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_items_route(self):
        # Test with items present in items.json
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Python Book', response.data)
        self.assertIn(b'Flask Mug', response.data)
        self.assertIn(b'Jinja Sticker', response.data)

    def test_empty_items(self):
        # Test with empty items list in items.json
        # Modify items.json temporarily
        with open('items.json', 'w') as f:
            f.write('{"items": []}')

        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No items found', response.data)

        # Restore items.json to original content
        with open('items.json', 'w') as f:
            f.write('{"items": ["Python Book", "Flask Mug", "Jinja Sticker"]}')

if __name__ == '__main__':
    unittest.main()
