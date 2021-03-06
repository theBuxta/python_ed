from random import *

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" \n'
            'Основные правила игры: \n'
            'Нам будет дано некоторое количество конфет, \n'
            'за один ход мы можем взять не более определённого количества, \n'
            'о котором мы с вами договоримся.\n'
            'Выигрывает тот, кто взял последние конфеты!\n'
            'Итак, начнём!\n')

messages = ['ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'ваш ход']


def candy(n):  # выбираем окончание для слова конфеты
    if n == 1 or n % 10 == 1:
        return 'а'
    elif 1 < n < 5 or 1 < n % 10 < 5:
        return 'ы'
    else:
        return ''


def play_game(n, m, players, messages):

    count = randint(0, 1)  # случайным образом выбираем кто ходит первым

    print(f'Первым ходит {players[count]}')

    while n > 0:
        # просим взять конфеты, проверяем правильное ли количество
        print(f'{players[count]}, {choice(messages)}')
        move = int(input())

        if move > n or move > m:
            print(
                f'Это слишком много, можно взять не более {m} конфет{candy(m)}, у нас всего {n} конфет{candy(n)}')

            # даём 3 попытки на взятие правильного количества конфет
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')

        n = n - move  # вычисляем остаток конфет
        if n > 0:
            print(f'Осталось {n} конфет{candy(n)}')
        else:
            print('Все конфеты разобраны.')

        count = (count + 1) % 2  # переход хода к следующему игроку

    return players[not count]


print(greeting)

player1 = input(
    'Давайте познакомися. Первый игрок, как к Вам можно обращаться? ')
player2 = input('Второй игрок, и Вы представьтесь, пожалуйста: ')
players = [player1, player2]

n = int(input('Сколько конфет будем разыгрывать?  '))
m = int(input('Сколько максимально будем брать конфет за один ход? '))

winer = play_game(n, m, players, messages)
print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!\n')