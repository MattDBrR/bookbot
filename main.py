from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        book = get_book_text(book_path)
        print("=========== BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        num_words = get_num_words(book)
        print("--------- Character Count -------")

        char_count = get_num_char(book)
        sorted_chars = sort_char_count(char_count)  

        for item in sorted_chars:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
