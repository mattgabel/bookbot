def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_dict = {}
    for character in text.lower():
        # If the key exists, increment it. If not, set it to 1
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict

def sort_char_dict(char_dict):
    list_of_dicts = []
    for key, value in char_dict.items():
        if key.isalpha() == True:
            item = {"char": key, "num": value}
            list_of_dicts.append(item)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(items):
    return items["num"]