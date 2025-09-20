import string
import random
import nltk
from nltk.corpus import words


def generate_random_password(length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
    password = string.ascii_letters
    if include_numbers:
        password += string.digits
    if include_symbols:
        password += string.punctuation

    return ''.join([random.choice(password) for _ in range(length)])


def generate_pin(length: int = 8):
    if not length:
        length = string.digits
        return length
    return ''.join([random.choice(string.digits) for _ in range(length)])


def generate_memorable_password(
        number_of_word: int = 4,
        vocab: list = 4,
        seperate: str = "-",
        captalize: bool = False
    ):
        vocab = nltk.corpus.words.words()
        if not vocab:
            vocab
        if captalize:
            return seperate.join([random.choice(vocab).upper() for _ in range(number_of_word)])
        
        return seperate.join([random.choice(vocab).upper() if random.choice([True, False]) else random.choice(vocab).lower() for _ in range(number_of_word)])


def main():
    print("Test for Pin password: ")
    print(generate_pin())
    print("\nTest for Generate password: ")
    print(generate_random_password())
    print("\nTest for Memorable password: ")
    print(generate_memorable_password(captalize=False))


if __name__ == "__main__":
    main()
