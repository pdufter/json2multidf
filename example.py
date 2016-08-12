from json2multidf import json2multidf

json_file = 'data/business.json'

import time
t = time.time()
example_dataframe = json2multidf(json_file)
result = time.time() - t

print result
print (example_dataframe)



