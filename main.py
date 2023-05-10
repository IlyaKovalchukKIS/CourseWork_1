from random import choice


def random_word(words: list):
    result = choice(words)
    return result
    
    
def encode_word(word: str, morse: list):
    for key, value in morse.items():
        
