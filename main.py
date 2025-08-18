from stats import get_num_words

from stats import word_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text('books/frankenstein.txt')
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")
    num_of_characters = word_counter(text)
    print (num_of_characters)

if __name__ == "__main__":
    main()

