def main():
    file_path = "books/frankenstein.txt"
    text = get_text_from_file(file_path)
    words = get_words_count(text)
    char_dict = get_chars_dict(text)
    char_sorted_list = convert_dict_list(char_dict)
    print_report(file_path, words, char_sorted_list)

def get_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()

def get_words_count(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for word in text:
        chars[word.lower()] = 0
    for word in text:
        chars[word.lower()] += 1
    return chars

def sort_on(dict):
    return dict["num"]

def convert_dict_list(dict):
    chars = []
    for char in dict:
        chars.append({"name": char, "num": dict[char]})
    chars.sort(reverse=True, key=sort_on)
    return chars

def print_report(file_path, num_words, chars_list):
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for c in chars_list:
        char = c["name"]
        char_count = c["num"]
        if char.isalpha():
            print(f"The '{char}' character was found {char_count} times")
    
    print("--- End report ---")

main()