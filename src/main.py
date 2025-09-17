import random
import string
import nltk
from abc import ABC, abstractmethod

nltk.download('words')

class PasswordGenerator(ABC):
    @abstractmethod
    def generator(self):
        pass


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.charecters = string.ascii_letters
        if include_numbers :
            self.charecters += string.digits
        if include_symbols :
            self.charecters += string.punctuation
            
    def generator(self):
        return ''.join([random.choice(self.charecters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
            self,
            number_of_words: int = 4,
            separator: str = "-",
            capitalize: bool = False,
            vocabulary: list = None
    ):
        if vocabulary is None :
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalize = capitalize
        
    def generator(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalize :
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words ]

        return self.separator.join(password_words)


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int = 8):
        self.length = length    
    
    def generator(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


def test_random_password_generator():
    random_gen = RandomPasswordGenerator(length=10, include_numbers=True, include_symbols=True)
    password = random_gen.generator()
    print(password)


def test_memorable_password_generator():
    memorable_gen = MemorablePasswordGenerator(
        number_of_words=4,
        separator="-",
        capitalize=True,
        vocabulary=nltk.corpus.words.words(),
    )
    password = memorable_gen.generator()
    print(password)


def test_pincode_generator():
    pin_gen = PinGenerator(length=4)
    pin = pin_gen.generator()
    print(pin)


def main():
    print("\nTesting RandomPasswordGenerator:")
    test_random_password_generator()
    print("\nTesting MemorablePasswordGenerator:")
    test_memorable_password_generator()
    print("\nTesting PinCodeGenerator:")
    test_pincode_generator()


if __name__ == "__main__":
    main()