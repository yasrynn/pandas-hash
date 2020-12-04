# pandas-hash

## A library for hashing pandas objects

This is a small library for hashing pandas objects. Not "hashing" in the Python sense of computing a hash once and for all for an immutable object, but in the [computer science sense](https://en.wikipedia.org/wiki/Hash_function).

But wait, you say, doesn't `pandas.util.hash_pandas_object` already do this? Sort of, but hashes of that sort don't detect subtle changes like the name of a `DataFrame` index changing.
