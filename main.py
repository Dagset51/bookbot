def get_book_text():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text

def main():
    text = get_book_text()
    print(text)

main()