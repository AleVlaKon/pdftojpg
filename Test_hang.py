def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')

    print(word_completion)
    word_split = list(word)
    word_completion = list(word_completion)

    while guessed is False:
        char = input()
        if char in word:                                               # если буква в слове есть
            for i in range(len(word_split)):
                if char == word_split[i]:
                    word_completion[i] = char
        print(word_completion)


play('КОЛБАСА')