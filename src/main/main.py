import os.path

from src.utils.utils import load_morse_alphabet, load_english_words, random_word, encode_word

ENGLISH_WORDS = os.path.abspath('../utils/english_words.txt')
MORSE_ALPHABET = os.path.abspath('../utils/morse_alphabet.json')


def main():
    morse_alphabet = load_morse_alphabet(MORSE_ALPHABET)
    english_words = load_english_words(ENGLISH_WORDS)
    print('Сегодня мы потренируемся расшифровывать азбуку Морзе\n'
          'Нажмите Enter и начнем')
    input()

    i = 0
    count_true = []

    while i != 5:
        i += 1
        english_words_random = random_word(english_words)
        morse_word = encode_word(english_words_random, morse_alphabet)
        print(english_words_random)
        user_input_encode = input(f'Слово {i}: {morse_word}')

        if user_input_encode in ['stop', 'стоп']:
            print(f'Вы угадали {count_true.count(True)} слов из 5')
            return

        if user_input_encode == english_words_random:
            count_true.append(True)
        else:
            print(f'неверно, правильное слово {english_words_random}')

    print(f'Вы угадали {count_true.count(True)} слов из 5')


if __name__ == '__main__':
    main()
