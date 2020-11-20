import unittest
from pandas_hash.pandas_hash import convert_hashable, hash_object

import os

class TestHash(unittest.TestCase):

    def test_hash_hashable(self):
        self.assertEqual(hash_object((1, 2)), hash((1, 2)))
        self.assertEqual(hash_object(frozenset((1, 2))), hash(frozenset((1, 2))))

    def test_hash_list(self):
        hsh = hash_object([1, 2])
        self.assertTrue(hsh)
        self.assertNotEqual(hash_object((1, 2)), hsh)

    def test_hash_set(self):
        hsh = hash_object({1, 2})
        self.assertTrue(hsh)
        self.assertNotEqual(hash_object(frozenset((1, 2))), hsh)
        