"""work2.py"""

def extract_words_starting_with_vowel(text):
    vowels = 'aeiouAEIOU'
    words = text.split()
    return [word for word in words if word[0] in vowels]

if __name__ == "__main__":
    text = input("Введите текст: ")
    words = extract_words_starting_with_vowel(text)
    print(words)
