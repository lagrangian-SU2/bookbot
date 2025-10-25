def count_words(string):
    return len(string.split())

def count_characters(string):
    result = {}
    for i in string.lower():
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    return result

def sort_dict(dict):
    list_of_pairs = [(i, j) for i, j in dict.items()]
    list_of_pairs = sorted(list_of_pairs, key=lambda x: x[1], reverse=True)
    list_of_dicts = [{'char': pair[0], 'num': pair[1]} for pair in list_of_pairs]
    return list_of_dicts