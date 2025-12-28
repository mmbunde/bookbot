import sys
from stats import get_num_words, get_num_letters, sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        f.close()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count -----------")
    book_text = get_book_text(path_to_book)
    get_num_words(book_text)
    print("----------- Character Count -----------")
    dict_char = get_num_letters(book_text)
    sort_char = sorted_list(dict_char)
    for item in sort_char:
        print(f"{item["char"]}: {item["num"]}")
    print("=========== End ===========")

main()