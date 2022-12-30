import unittest
from src.fun.search import search_anime

class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search_anime())