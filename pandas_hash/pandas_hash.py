from pandas import Series, DataFrame
from pandas.util import hash_pandas_object

class PandasObjectWrapper:
    def __init__(self, obj):
        self.obj = obj
        name = obj.name if hasattr(obj, 'name') else None
        index_name = obj.index.name if hasattr(obj, 'index') else None
        columns_name = obj.columns.name if hasattr(obj, 'columns') else None
        self.index_names = (name, index_name, columns_name)

    def __hash__(self):
        return hash((
            tuple(hash_pandas_object(self.obj).tolist()),
            hash(self.index_names),
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
        elif isinstance(obj, Series) or isinstance(obj, DataFrame):
            out_obj = PandasObjectWrapper(obj)
        else:
            raise TypeError(f"Don't know how to convert object of type {type(obj)} to hashable")
        # elif hasattr(obj, '__dict__'):
            # return convert_hashable(obj.__dict__)
        return out_obj
    else:
        return obj

def hash_object(obj):
    return hash((type(obj), convert_hashable(obj)))