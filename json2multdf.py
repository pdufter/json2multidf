import json
import pandas


def decrease_dict_levels(nested_dict):
    # returns flattened dict with tuples as keys
    resulting_dict = {}
    list_of_levels = [[nested_dict.items()]]
    previous_parent_keys = [tuple()]
    for level in list_of_levels:
        new_level = list()
        parent_keys = list()
        subdict_counter = 0
        for subdict in level:
            for key, value in subdict:
                if isinstance(value, dict):
                    parent_keys.append(previous_parent_keys[subdict_counter] + (key,))
                    new_level.append(value.items())
                else:
                    resulting_dict[previous_parent_keys[subdict_counter] + (key,)] = value
            subdict_counter = subdict_counter + 1
        if new_level != list():
            list_of_levels.append(new_level)
        previous_parent_keys = parent_keys
    return resulting_dict


def convert_json2multidf(path_to_json, create_multiindex=True):
    # inputs json data, flattens it and returns multiindex dataframe
    with open(path_to_json, 'r') as json_data:
        result = pandas.DataFrame(decrease_dict_levels(json.loads(line)) for line in  json_data)
    if create_multiindex is True:
        current_index = standardise_tuple_length(list(result.columns))
        multiindex = pandas.MultiIndex.from_tuples(current_index)
        result.columns = multiindex
    return result


def standardise_tuple_length(list_of_tuples):
    # multiindex is required to be homogenous, thus standardise the tuple length
    max_length = max([len(item) for item in list_of_tuples])
    standardised_tuples = [item + tuple([''] * (max_length - len(item))) for item in list_of_tuples]
    return standardised_tuples


if __name__ == '__main__':
    
    json_file = 'data/fake_data.json'

    example_dataframe = convert_json2multidf(json_file)
    print (example_dataframe)
