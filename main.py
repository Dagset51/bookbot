from stats import count_words
from stats import count_characters

def get_book_text():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text
    

def main():
    text = get_book_text()
    num_words = count_words(text)
    characters = count_characters(text)
    print(f"{num_words} words found in the document")

main()
