def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Word count: {num_words}")
    num_letters = get_num_letters(text)
    print(f"Letter count: {num_letters}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_count = {letter: 0 for letter in alphabet}

    for char in text:
        normalized_letter = char.lower()
        if normalized_letter in alphabet:
            letter_count[normalized_letter] += 1
    return letter_count
    
main()