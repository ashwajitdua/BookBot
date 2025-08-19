def get_num_words(text):
    words = text.split()
    count= len(words) 
    return count

def word_counter(text):
    character_counter = {}
    for character in text:
        character = character.lower()
        if character in character_counter:
            character_counter [character] += 1
        else:
            character_counter [character] = 1
    return character_counter

def sorted_list(character_dictionary):
    Sorted_dictionaries = []
    for char, char_count in character_dictionary.items():
        num_dictionary = {"char": char, "num": char_count}
        Sorted_dictionaries.append(num_dictionary)
    Sorted_dictionaries.sort(reverse=True, key= lambda char: char["num"])
    return Sorted_dictionaries


