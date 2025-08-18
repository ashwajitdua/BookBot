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
        