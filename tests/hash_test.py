import unittest
import pandas as pd
from pandas_hash.pandas_hash import convert_hashable, hash_object

class TestHash(unittest.TestCase):

    def test_hash_hashable(self):
        obj = (1, 2)
        rev_tuple = (2, 1)
        self.assertTrue(hash_object(obj))
        self.assertNotEqual(hash_object(obj), hash_object(rev_tuple))
        self.assertTrue(hash_object(frozenset(obj)))

    def test_hash_list(self):
        obj = [1, 2]
        obj_rev = list(reversed(obj))
        self.assertTrue(hash_object(obj))
        self.assertNotEqual(hash(convert_hashable(obj)), hash_object(obj))
        self.assertNotEqual(hash_object(obj), hash_object(obj_rev))

    def test_hash_set(self):
        obj = {1, 2}
        self.assertTrue(hash_object(obj))
        self.assertNotEqual(hash(convert_hashable(obj)), hash_object(obj))

    def test_hash_dict(self):
        obj = dict(a='hello', b='there')
        obj_rev = dict(b='there', a='hello')
        self.assertTrue(hash_object(obj))
        self.assertNotEqual(hash(convert_hashable(obj)), hash_object(obj))
        # For now I guess differently ordered dicts should be hashed the same
        self.assertEqual(hash_object(obj), hash_object(obj_rev)) 

    def test_hash_pandas(self):
        df = pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], name='hello'))
        df2 = pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], name='hello2'))
        self.assertTrue(hash_object(df))
        self.assertNotEqual(hash_object(df), hash_object(df2))
        self.assertNotEqual(hash_object(df), hash_object(df.rename_axis('newindex', axis=0)))
        self.assertNotEqual(hash_object(df), hash_object(df.rename_axis('newcolumns', axis=1)))
