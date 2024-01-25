def main():
    file_path = "./books/frankenstein.txt"
    text = get_text_from_file(file_path)
    num_words = get_num_words(text)
    print(num_words)

def get_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

main()