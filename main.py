def read_file(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def book_report(book_name):
    text = read_file(f'books/{book_name}')
    word_count = count_words(text)
    character_count = count_characters(text)
    print(f'--- Begin report of books/{book_name} ---')
    print(f'{word_count} words found in the document')
    print()
    for char in sorted(character_count):
        print(f'The {char} character was found {character_count[char]} times')
    print('--- End report ---')

def __main__():
    book_report('frankenstein.txt')

__main__()

