def main():
    file_path = "./books/frankenstein.txt"
    text = get_text_from_file(file_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"words count: {num_words}")
    print(f"characters count: {chars_dict}")

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

main()