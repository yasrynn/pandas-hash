import pandas as pd
from hashlib import sha256
from pandas.util import hash_pandas_object

class PandasDataFrameWrapper:
    def __init__(self, obj):
        self.obj = obj

    def __hash__(self):
        return hash((
            int(sha256(hash_pandas_object(self.obj).values).hexdigest(), 16),
            hash(self.obj.index.name),
            hash(self.obj.columns.name)
        ))


def convert_hashable(obj):
    try:
        hash(obj)
    except TypeError:
        if type(obj) is list:
            out_obj = tuple(convert_hashable(i) for i in obj)
        elif type(obj) is set:
            out_obj = frozenset(convert_hashable(i) for i in obj)
        elif type(obj) is dict:
            out_obj = frozenset((k, convert_hashable(v)) for k,v in obj.items())
        elif isinstance(obj, pd.DataFrame):
            out_obj = PandasDataFrameWrapper(obj)
        else:
            raise TypeError(f"Don't know how to convert object of type {type(obj)} to hashable")
        # elif hasattr(obj, '__dict__'):
            # return convert_hashable(obj.__dict__)
        return out_obj
    else:
        return obj

def hash_object(obj):
    return hash((type(obj), convert_hashable(obj)))