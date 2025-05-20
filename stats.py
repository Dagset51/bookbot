def count_words(text):
    words = text.split()
    total = len(words)
    return total

def count_characters(text):
    lower_case = str.lower(text)
    characters = {}
    for lower_case in lower_case:
        characters[lower_case] += 1
    return characters