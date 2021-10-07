import random


def define_operation(select):
    if select == 1:
        return '+'
    elif select == 2:
        return '-'
    else:
        return '*'


def calculate_answer(numbers, oper):
    if oper == '-':
        return numbers[0] - numbers[1]
    elif oper == '+':
        return numbers[0] + numbers[1]
    else:
        return numbers[0] * numbers[1]


def define_difficulty(diff):

    if diff == '1':
        return 10
    elif diff == '2':
        return 100
    elif diff == '3':
        return 1000
    elif diff == '4':
        return 10000
    else:
        print('Invalid option, difficulty set to 1')
        return 10


def play(points, max_number):

    operation = define_operation(random.randint(1, 3))

    nums = [random.randint(0, max_number), random.randint(0, max_number)]
    print(f'{nums[0]} {operation} {nums[1]} = ?')
    result = calculate_answer(nums, operation)

    answer = int(input('\nType your answer: '))

    if answer == result:
        points += 1
        print(f'Correct answer. Your score is {points}')
    else:
        print(f'Incorrect answer. Your score is {points} ')

    option = int(input('Type 1 to keep playing, 2 to change difficulty or anything else to exit: \n'))
    if option == 1:
        play(points, max_number)
    elif option == 2:
        diff = input('Choose the difficulty - 1, 2, 3 or 4: ')
        max_number = define_difficulty(diff)
        play(points, max_number)


class Game:

    @staticmethod
    def start():
        difficulty = input('Choose the difficulty - 1, 2, 3 or 4: \n')
        play(0, define_difficulty(difficulty))


if __name__ == '__main__':
    Game.start()





