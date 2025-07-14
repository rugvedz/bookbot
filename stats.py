def number_of_words(text):
    word_list = text.split()
    return len(word_list)

def count_character_occurence(text):
    character_dict = {}

    for character in text:
        if character.lower() not in character_dict.keys():
            character_dict[character.lower()] = 1
        else:
            character_dict[character.lower()] += 1
    return character_dict

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    formatted_dict = []
    for key in char_dict.keys():
        obj = {}
        obj["char"] = key
        obj["num"] = char_dict[key]
        formatted_dict.append(obj)

    formatted_dict.sort(reverse=True, key=sort_on)

    return formatted_dict