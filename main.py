import re

def count_words(string):
    return len(string.split())

def characters_counter(string, lower=True):
    result = {}
    if lower:
        string = string.lower()
    dont_count = '\n .#'
    for c in string:
        if c in dont_count:
            continue
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result


path = './books/frankenstein.txt'
with open(path) as f:
    file_contents = f.read()

print(f'--- Begin report of {path} ---')
print(f'{count_words(file_contents)} was found in the document')
counter = characters_counter(file_contents)
for k, v in counter.items():
    print(f"The character '{k}' was found {v} times")
print('--- End report ---')
