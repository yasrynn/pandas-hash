import unittest
import pandas as pd
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
        
    def test_hash_pandas(self):
        hsh = hash_object(pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], name='hello')))
        hsh2 = hash_object(pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], name='hello2')))
        self.assertTrue(hsh)
        print(hsh)
        print(hsh2)
        self.assertNotEqual(hsh, hsh2)