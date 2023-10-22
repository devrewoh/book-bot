def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"Word count: {word_count}")
    letter_count = count_letters(text)
    print(f"Letter count: {letter_count}")

    #letter_count = count_letters(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in alphabet:
        letter_count[letter] = 0
        for char in text:
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
    return letter_count
    
main()