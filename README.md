# json2multidf
Code snippet which flattens nested dictionarys. As such it offers the functionality to directly convert json data to a multindexed pandas dataframe.

# Usage

Download json2multidf.py and use as shown in the example.py.

# Performance Comparison
Most code snippets for flattening a dictionary are recursion based (e.g. http://codereview.stackexchange.com/questions/21033/flatten-dictionary-in-python-functional-style).
While a non-recursive formulation is syntactically not as nice, it offers better performance in Python (especially on larger and more deeply nested json files).


| [s]           | Fake dataset | Yelp dataset  |
| ------------- |:------------:|:-------------:|
| Non-recursive | 3.1979       | 7.2744        |
| Recursive 1   | 3.4391       | 8.8872        |
| Recursive 2   | 3.5939       | 9.7790        |
