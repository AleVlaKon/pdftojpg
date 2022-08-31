import random

word_list = ['колбаса', 'кола', 'печенье']


def get_word(x):
    """Выбирает случайный элемент из списка слов и делает его заглавным"""
    i = random.randint(0, len(x) - 1)
    return x[i].upper()


def display_hangman(tries):
    """Показывает виселицу в зависимости от количества попыток"""
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def char_input():
    """ Проверяет, чтобы вводились только буквы, иначе просит вводить заново"""

    char = input('Введите букву или слово')
    if char.isalpha():
        return char.upper()
    else:
        print('Введи букву или слово, никаких цифр!!!')
        char_input()


def after_turn(tries, word_completion):
    """Печатает виселицу
       Печатает слово с пропусками"""
    print(display_hangman(tries))
    print(*word_completion)



def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(6))
    print(word_completion)
    word_split = list(word)
    word_completion = list(word_completion)

    while not guessed and tries > 0:

        char = char_input()

        if char == word and len(char) > 1:					# Если угадал слово
            guessed = True

        elif char in guessed_letters:
            print('Ты уже называл эту букву, попробуй еще')

        elif char in guessed_words:
            print('Ты уже называл это слово, попробуй еще')

        elif char != word and len(char) > 1:					    # Если не угадал слово
            tries -= 1						                        # Количество попыток уменьшается на 1
            guessed_words.append(char)			                    # добавление в перечень уже названных слов
            print("Ты не угадал, и все ближе к смерти")
            after_turn(tries, word_completion)                      # Показать виселицу

        elif char not in word:
            tries -= 1                                              # Количество попыток уменьшается на 1
            guessed_letters.append(char)                            # добавление в перечень уже названных букв
            print("Ты не угадал, и все ближе к смерти")
            after_turn(tries, word_completion)                      # Показать виселицу

        elif char in word:                                          # если буква в слове есть
            for i in range(len(word_split)):                              # собираем слово с угаданной буквой
                if char == word_split[i]:
                    word_completion[i] = char
                after_turn(tries, word_completion)
        if "_" not in word_completion:
            guessed = True
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')
                

again = 'д'

while again.lower() == 'д':
    word = get_word(word_list)
    play(word)
    again = input('Играем еще раз? (д = да, н = нет):')




        











