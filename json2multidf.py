import json
import pandas
import itertools


def decreaseDictLevels(nested_dict):
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


def json2multidf(path_to_json, create_multiindex=True):
    # inputs json data, flattens it and returns multiindex dataframe
    with open(path_to_json, 'r') as json_data:
        result = pandas.DataFrame(decreaseDictLevels(json.loads(line)) for line in  json_data)
    if create_multiindex is True:
        current_index = standardiseTupleLength(list(result.columns))
        multiindex = pandas.MultiIndex.from_tuples(current_index)
        result.columns = multiindex
    return result


def standardiseTupleLength(list_of_tuples):
    # multiindex is required to be homogenous, thus standardise the tuple length
    max_length = max([len(item) for item in list_of_tuples])
    standardised_tuples = [item + tuple([''] * (max_length - len(item))) for item in list_of_tuples]
    return standardised_tuples


def convertListsToDummies(pandas_series):
    # pivot and create dummys for list entries
    tmp_sep = "_.-:-._"

    unique_headers = list(set(
        itertools.chain(
            *list(pandas_series)
            )
        ))

    all_dummies = pandas_series.apply(pandas.Series)
    all_dummies = pandas.get_dummies(all_dummies, prefix_sep=tmp_sep)

    # we might have some duplicated columns thus reduced them to a single column
    reduced_dummies = pandas.DataFrame()
    for entry in unique_headers:
        sel_cols = [entry in column_header for column_header in all_dummies.columns]
        reduced_dummies[entry] = all_dummies.ix[:, sel_cols].sum(axis=1).apply(bool)

    return reduced_dummies


if __name__ == '__main__':
    
    json_file = 'data/fake_data.json'

    example_dataframe = json2multidf(json_file)
    print ('\n\nResulting multiindex dataframe:\n')
    print (example_dataframe)
    
    print ('\n\nExample for list conversion:\n')
    print ('Before')
    print (example_dataframe[('beer_menu', 'lager')])
    print ('After')
    print (convertListsToDummies(example_dataframe[('beer_menu', 'lager')]))

