"""
Бейглз, (c) Эл Свейгарт al@inventwithpython.com
"""
import random
import config


def run_game():
    """
    Дедуктивная логическая игра на угадывание числа по подсказкам.
    Код размещен на https://nostarch.com/big-book-small-python-projects
    Один из вариантов этой игры приведен в книге Invent Your Own
    Computer Games with Python на https://nostarch.com/inventwithpython
    Теги: короткая, игра, головоломка
    """
    print(f'''Bagels, a deductive logic game.
            By Al Sweigart al@inventwithpython.com

            Описание работы

            I am thinking of a {config.NUM_DIGITS}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say:    That means:
            Pico         One digit is correct but in the wrong position.
            Fermi        One digit is correct and in the right position.
            Bagels       No digit is correct.

            For example, if the secret number was 248
            and your guess was 843, the
            clues would be Fermi Pico.''')

    while True:
        secret_num = get_secretnum()
        print('I have thought up a number.')
        print(f' You have {config.MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= config.MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до получения правильной догадки:
            while len(guess) != config.NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # Правильно, выходим из цикла.
            if num_guesses > config.MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {secret_num}.')

        # Спрашиваем игрока, хочет ли он сыграть еще раз.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secretnum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')  # Создает список цифр от 0 до 9.
    random.shuffle(numbers)  # Перетасовываем их случайным образом.

    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа:
    secret_num = ''
    for i in range(config.NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа."""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i, digit in enumerate(guess):
        if digit == secret_num[i]:
            # Правильная цифра на правильном месте.
            clues.append('Fermi')
        elif digit in secret_num:
            # Правильная цифра на неправильном месте.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # Правильных цифр нет вообще.
        # Сортируем подсказки в алфавитном порядке, чтобы их исходный
        # порядок ничего не выдавал.
    clues.sort()
    return ' '.join(clues)
