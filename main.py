from stats import number_of_words
from stats import symbol_calculator
from stats import sort_values
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        words = text.split()
        num_chars = number_of_words(words)
        symbol_dict =(symbol_calculator(text))
        sorted_dict = sort_values(symbol_dict)
        print("============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f'Found {num_chars} total words')
        print("--------- Character Count -------")
        for i in sorted_dict:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")

main()
