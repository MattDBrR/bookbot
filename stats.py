def get_num_words(book):
    result = book.split()
    num = len(result)
    print("Found",num, "total words")

def get_num_char(book):
    result = book.lower()
    char_count = {} # Use a dictionary
    for char in result:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_char_count(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
