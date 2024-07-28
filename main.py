def main():
    file_path = "books/frankenstein.txt"
    text = get_text_from_file(file_path)
    words = get_words_count(text)
    print(words)
    char_dict = get_chars_dict(text)
    print(char_dict)

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

main()