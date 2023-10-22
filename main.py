def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    letter_list = list(num_letters.items())
    sorted_letter_counts = sorted(letter_list, key=lambda x:x[1], reverse = True)
    print(f"------ Begin report of {book_path} ------")
    print(f"{num_words} words found in the document")
    print()
    for letter, count in sorted_letter_counts:
        print(f"The letter '{letter}' was found {count} times")
    print(f"------ End report ------")
    

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