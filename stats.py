
def number_of_words(words):
    num_words = 0
    for i in words:
        num_words += 1
    return num_words

def symbol_calculator(text):
    symbol_dict = {}
    text_low = text.lower()
    for i in text_low:
        if i not in symbol_dict:
            symbol_dict[i] = 1
        elif i in symbol_dict:
            symbol_dict[i] += 1
    return symbol_dict

def sort_on(dict):
    return dict["num"]

def sort_values(num_chars):
    new_dict = {}
    list = []
    for k, v in num_chars.items():
        new_dict = {"char": k, "num": v}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list
