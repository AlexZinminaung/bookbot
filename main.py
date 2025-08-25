from stats import get_words, get_chars, dict_to_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    text = get_book_text(sys.argv[1])
    count = len(get_words(text))
    chars = get_chars(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char in dict_to_list(chars):
        print(str(char['char']) + ": " + str(char['num']))
    print("============= END ===============")

main()