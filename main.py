def get_book_text(file):
    with open(file) as f:
        book_contents = f.read()
        return book_contents

def num_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = num_words(text)
    print(f"{word_count} words found in the document")

main()