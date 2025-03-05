def num_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_chars(text):
    chars_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict



def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    list_of_dicts = []
    for key, value in dict.items():
        if key.isalpha():
            list_of_dicts.append({"char": key, "num": value})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

