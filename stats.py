def get_words(words):
    num_words = words.split()
    return num_words

def get_chars(words):
    lower_word = words.lower()
    new_dict = {}

    for char in lower_word:
        if char not in new_dict:
            new_dict[char] = 1
        else:
            new_dict[char] += 1

    
    return new_dict

def sort_on(items):
    return items["num"]

def dict_to_list(dict):
    new_list = []

    for item in dict:
        new_dict = {}
        new_dict["char"] = item
        new_dict["num"] = dict[item]
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    
    return new_list
