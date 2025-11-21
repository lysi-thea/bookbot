from stats import (
    get_num_words,
    get_num_chars,
    get_sorted_list
)
import sys

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    return file_contents

def print_report(book_path, num_words, chars_sorted_list):
    print("\n\n============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in chars_sorted_list:
        if not dict["char"].isalpha():
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============\n")

def check_sys_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_sys_args()
    book_path = sys.argv[1]
    story_content = get_book_text(book_path)
    num_words = get_num_words(story_content)
    dict_char_num = get_num_chars(story_content)
    chars_sorted_list = get_sorted_list(dict_char_num)

    print_report(book_path, num_words, chars_sorted_list)

if __name__ == "__main__":
    main()
