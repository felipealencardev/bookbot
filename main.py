def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = get_words_count(file_contents)
        print(words)

def get_words_count(file_contents):
    return len(file_contents.split())

main()