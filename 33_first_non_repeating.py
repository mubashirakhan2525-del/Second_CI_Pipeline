
def first_non_repeating(text):
    for character in text:
        if text.count(character) == 1:
            return character

    return None
