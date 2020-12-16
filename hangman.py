import random
from word_ru import words_ru


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words_ru)
    word_letters = set(word)
    alphabet = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    used_letters = set()

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('У вас осталось', lives, 'жизней и вы уже пробовали следующие буквы: ', ' '.join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Угадайте букву: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Нет такой буквы')
        elif user_letter in used_letters:
            print('Вы уже пробовали эту букву, попробуйте другую.')
        else:
            print('Неверная буква, попробуйте ещё раз.')
    if lives == 0:
        print('Жизни закончились! Было загадано слово', word )
    else:
        print('Вы угадали слово', word, '!!!')


hangman()

