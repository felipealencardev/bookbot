def main():
    file_path = "books/frankenstein.txt"
    text = get_text_from_file(file_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = get_chars_sorted_list(chars_dict)

    print_report(file_path, num_words, chars_sorted_list)

def get_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(words):
    chars = {}
    for word in words:
        chars[word.lower()] = 0

    for word in words:
        chars[word.lower()] += 1
    
    return chars

def get_chars_sorted_list(chars_dict):
    return sorted(list(chars_dict.items()), key=lambda char: char[0])

def print_report(file_path, num_words, chars_list):
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for c in chars_list:
        char = c[0]
        char_count = c[1]
        if char.isalpha():
            print(f"The '{char}' character was found {char_count} times")
    
    print("--- End report ---")
main()