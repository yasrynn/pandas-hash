import unittest
import pandas as pd
from pandas_hash.pandas_hash import convert_hashable, hash_object

import os

class TestHash(unittest.TestCase):

    def test_hash_hashable(self):
        obj = (1, 2)
        rev_tuple = (2, 1)
        self.assertTrue(hash_object(obj))
        self.assertNotEqual(hash_object(obj), hash_object(rev_tuple))
        self.assertTrue(hash_object(frozenset(obj)))

    def test_hash_list(self):
        obj = [1, 2]
        hsh = hash_object(obj)
        self.assertTrue(hsh)
        self.assertNotEqual(hash(convert_hashable(obj)), hsh)

    def test_hash_set(self):
        obj = {1, 2}
        hsh = hash_object(obj)
        self.assertTrue(hsh)
        self.assertNotEqual(hash(convert_hashable(obj)), hsh)

    def test_hash_dict(self):
        obj = dict(a='hello', b='there')
        hsh = hash_object(obj)
        self.assertTrue(hsh)
        self.assertNotEqual(hash(convert_hashable(obj)), hsh)

    def test_hash_pandas(self):
        df = pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], name='hello'))
        hsh = hash_object(df)
        hsh2 = hash_object(pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], name='hello2')))
        self.assertTrue(hsh)
        print(hsh)
        print(hsh2)
        self.assertNotEqual(hsh, hsh2)
        self.assertNotEqual(hsh, hash_object(df.rename_axis('newindex', axis=0)))
        self.assertNotEqual(hsh, hash_object(df.rename_axis('newcolumns', axis=1)))
