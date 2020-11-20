import pandas as pd

def convert_hashable(obj):
    try:
        hash(obj)
    except TypeError:
        if type(obj) is list:
            return tuple(convert_hashable(i) for i in obj)
        elif type(obj) is set:
            return frozenset(convert_hashable(i) for i in obj)
        elif type(obj) is dict:
            return frozenset((convert_hashable(k), convert_hashable(v)) for k,v in obj.items())
        elif hasattr(obj, __dict__):
            return convert_hashable(obj.__dict__)
    else:
        return obj

def hash_object(obj):
    try:
        return hash(obj)
    except TypeError:
        return hash(type(obj)) ^ hash(convert_hashable(obj))