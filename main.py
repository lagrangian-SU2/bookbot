import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        out = file.read()
    return out

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    n = count_words(text)
    counter = count_characters(text)
    result = sort_dict(counter)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {n} total words')
    print('--------- Character Count -------')
    for i in result:
        if i['char'].isalpha():
            print(f'{i["char"]}: {i["num"]}')
    print('============= END ===============')

if __name__=='__main__':
    main()