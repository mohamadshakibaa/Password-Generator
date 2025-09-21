# Python Password Generator - Functional Approach
Welcome to the python password generator project - Functional Programming constructs such as functions, instead of classes(Object Oriented Programming)

The password generator creates:

1. Random Passwords
2. Oin Codes
3. Memorable Passwords

## How It Works
The password generator uses Python's `random` and `string` modules to generate passwords based on user preferences. The generator consists of three distinct functions, each representing a different type of password generation:

1. `generate_random_password` creates a random password with specified length, and includes numbers and/or special characters based on your preference.
2. `generate_pin` produces a numeric pin code of a specified length.
3. `generate_memorable_password` generates a password composed of a number of random words selected from an English language corpus. You can specify the separator and whether the words should be capitalized.

## Requirements
- Python 3.7+
- NLTK (Natural Language Toolkit)

To install NLTK, use pip:
```puthon
pip install nltk
```
After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:
```python
import nltk
nltk.download('words')
```
That's all you need to know to get started with this project. Enjoy generating passwords!