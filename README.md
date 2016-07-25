# json2multidf
Small helper function which flattens nested json files and converts it to multindex pandas dataframes.

# Usage

Download json2multidf.py and use as shown in the example.py.

# Performance Comparison
Many solutions using recursions are available (e.g. http://codereview.stackexchange.com/questions/21033/flatten-dictionary-in-python-functional-style).
A quick performance comparison, however, shows that the non-recursive formulation is faster (especially on larger and more nested json files).

FAKE DATA SET
('Non-recursive:', 3.197918176651001)
('Recursive 1:', 3.43914794921875)
('Recursive 2:', 3.5939371585845947)

YELP BUSINESS DATA SET
('Non-recursive:', 7.274427175521851)
('Recursive 1:', 8.88723087310791)
('Recursive 2:', 9.779070854187012)
