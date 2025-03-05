from stats import num_words, count_chars, dict_to_list
import sys

def get_book_text(file):
    with open(file) as f:
        book_contents = f.read()
        return book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path-to-book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    word_count = num_words(text)
    chars = count_chars(text)
    only_alpha = dict_to_list(chars)

    print(
f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    )
    for i in only_alpha:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()