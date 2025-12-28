def get_num_words(string):
    num_words = string.split()
    print(f"Found {len(num_words)} total words")

def get_num_letters(string):
    num_chars = {}

    for char in string.lower():
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars
    # return dict(sorted(num_chars.items(), key=lambda item: item[1], reverse=True))

def sort_on(item):
    return item["num"]

def sorted_list(dictionary):
    new_dictionary = []

    for char, count in dictionary.items():
        if not char.isalpha():
            continue
        new_dictionary.append({"char": char, "num": count})
    
    new_dictionary.sort(key=sort_on, reverse=True)
    return new_dictionary