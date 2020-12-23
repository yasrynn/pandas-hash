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

    def test_hash_dataframe(self):
        df = pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], str_col=['hello1', 'hello2', 'hello3']))
        df2 = pd.DataFrame(dict(column1=[1, 3, 5], column2=[2, 3, 5], str_col=['hello1', 'hello2', 'hello4']))
        self.assertTrue(hash_object(df))
        self.assertEqual(hash_object(df), hash_object(df))
        self.assertNotEqual(hash_object(df), hash_object(df2))
        self.assertNotEqual(hash_object(df), hash_object(df.rename_axis('newindex', axis=0)))
        self.assertNotEqual(hash_object(df), hash_object(df.rename_axis('newcolumns', axis=1)))
        self.assertNotEqual(hash_object(df), hash_object(df.set_index(pd.Index([2, 4, 6]))))
        self.assertNotEqual(hash_object(df), hash_object(df.set_index(pd.Index(['2', '4', '6']))))

    def test_hash_series(self):
        srs = pd.Series([6, 7, 8])
        srs = pd.Series([6, 7, 9])
        self.assertEqual(hash_object(srs), hash_object(srs))
        self.assertNotEqual(hash_object(srs), hash_object(srs2))
        self.assertNotEqual(hash_object(srs), hash_object(srs.rename('hello')))
        self.assertNotEqual(hash_object(srs.rename('hello')), hash_object(srs.rename('hello2')))
        self.assertNotEqual(hash_object(srs), hash_object(srs.rename_axis('hello')))
        self.assertNotEqual(hash_object(srs.rename_axis('hello')), hash_object(srs.rename_axis('hello2')))
        
        