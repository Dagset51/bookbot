def count_words(text):
    words = text.split()
    total = len(words)
    return total

def count_characters(text):
    lower_case = text.lower()
    characters = {}
    for char in lower_case:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    alphabet = characters.sort(char)
    return alphabet