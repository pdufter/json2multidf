# COMPARE TO BOTH FUNCTIONS FROM:
# http://codereview.stackexchange.com/questions/21033/flatten-dictionary-in-python-functional-style
# Credits to Winston Ewert
def flatten_dict_1(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict_1(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value

    return dict(items())

def flatten_dict_2(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (key + '.' + k, v) for k, v in flatten_dict_2(value).items() ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)

# tuple versions of both functions

def flatten_dict_1_tuple(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict_1_tuple(value).items():
                    yield (key,) + (subkey,), subvalue
            else:
                yield key, value

    return dict(items())

def flatten_dict_2_tuple(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ ((key,) + (k,), v) for k, v in flatten_dict_2_tuple(value).items() ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)


if __name__ == "__main__":
    # import my own function
    from json2multidf import *
    import timeit
    
    print ("FAKE DATA SET")
    print ("Non-recursive:", min(timeit.repeat("[decreaseDictLevels(json.loads(line)) for line in open('data/fake_data.json', 'r')]", 
                                setup="from json2multidf import decreaseDictLevels; import json; gc.enable()", 
                                number=100000, 
                                repeat=3)))
    print ("Recursive 1:", min(timeit.repeat("[flatten_dict_1_tuple(json.loads(line)) for line in open('data/fake_data.json', 'r')]", 
                               setup="from speed_comparison import flatten_dict_1_tuple; import json; gc.enable()", 
                               number=100000, 
                               repeat=3)))
    print ("Recursive 2:", min(timeit.repeat("[flatten_dict_2_tuple(json.loads(line)) for line in open('data/fake_data.json', 'r')]", 
                               setup="from speed_comparison import flatten_dict_2_tuple; import json; gc.enable()", 
                               number=100000, 
                               repeat=3)))
    
    # performance comparison on the business data set available from the Yelp Challenge
    print ()
    print ("YELP BUSINESS DATA SET")
    print ("Non-recursive:", min(timeit.repeat("[decreaseDictLevels(json.loads(line)) for line in open('data/business.json', 'r')]", 
                                 setup="from json2multidf import decreaseDictLevels; import json; gc.enable()", 
                                 number=1, 
                                 repeat=3)))
    print ("Recursive 1:", min(timeit.repeat("[flatten_dict_1_tuple(json.loads(line)) for line in open('data/business.json', 'r')]", 
                               setup="from speed_comparison import flatten_dict_1_tuple; import json; gc.enable()", 
                               number=1, 
                               repeat=3)))
    print ("Recursive 2:", min(timeit.repeat("[flatten_dict_2_tuple(json.loads(line)) for line in open('data/business.json', 'r')]", 
                               setup="from speed_comparison import flatten_dict_2_tuple; import json; gc.enable()", 
                               number=1, 
                               repeat=3)))
 


