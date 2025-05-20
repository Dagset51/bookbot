from stats import count_words
from stats import count_characters

def get_book_text():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text
    

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    text = get_book_text()
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    characters = count_characters(text)
    print(characters)

main()
