import json
import os.path
from random import choice


def load_morse_alphabet(morse: str):
    with open(morse, 'r', encoding='utf-8') as f:
        file = json.load(f)
        return file


def load_english_words(words: str):
    with open(words, 'r', encoding='utf-8') as f:
        file = f.read()
        return eval(file)


def random_word(words: list):
    result = choice(words)
    return result


def encode_word(word: str, morse: dict):
    morse_word = ''
    for letter in word:
        morse_word += f"{morse.get(letter)} "

    return morse_word

