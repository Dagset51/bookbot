from stats import count_words
def get_book_text():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text
    

def main():
    text = get_book_text()
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

main()
