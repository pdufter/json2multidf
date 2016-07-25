# json2multidf
Small helper function which flattens nested json files and converts it to multindex pandas dataframes.

# Usage

Download json2multidf.py and use as shown in the example.py.

# Performance Comparison
Many solutions to flatten a dictionary using recursion are available (e.g. http://codereview.stackexchange.com/questions/21033/flatten-dictionary-in-python-functional-style).
A quick performance comparison, however, shows that the non-recursive formulation is faster (especially on larger and more nested json files).


| [s]           | Fake dataset | Yelp dataset  |
| ------------- |:------------:|:-------------:|
| Non-recursive | 3.1979       | 7.2744        |
| Recursive 1   | 3.4391       | 8.8872        |
| Recursive 2   | 3.5939       | 9.7790        |
