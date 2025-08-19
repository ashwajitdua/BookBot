from stats import get_num_words

from stats import word_counter

from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text('books/frankenstein.txt')
    word_count = get_num_words(text)
    num_of_characters = word_counter(text)
    my_sorted_char_list = sorted_list(num_of_characters)
    print ("============ BOOKBOT ============ ")
    print ("Analyzing book found at books/frankenstein.txt...") 
    print ("----------- Word Count ---------- ")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for num_dictionary in my_sorted_char_list:
        char = num_dictionary["char"]
        count = num_dictionary["num"]
        if char.isalpha() == True:
            print (f"{char}: {count}")    
    print ("============= END ===============")

if __name__ == "__main__":
    main()

