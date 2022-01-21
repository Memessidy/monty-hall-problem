import random


def get_negatives(doors):
    negatives = []
    while len(negatives) < 2:
        current = random.choice(doors)
        if current not in negatives:
            negatives.append(current)
        else:
            continue
    return negatives


def open_negative_door(negatives, choice):
    for x in negatives:
        if x in negatives and x != choice:
            return x


def get_positives(doors, negatives):
    for door in doors:
        if door not in negatives:
            return door


def change_choice(doors, negative_door_not_choice, choice, switch = True):
    if not switch:
        return choice
    for door in doors:
        if door != choice and door != negative_door_not_choice:
            return door


def run(switch):
    doors = [x for x in range(0, 3)] # Все двери
    negatives = get_negatives(doors=doors) # Двери, за которыми нет приза
    positive = get_positives(doors, negatives) # Дверь, за которой есть приз
    choice = random.choice(doors) # Выбор игрока
    negative_door_not_choice = open_negative_door(negatives, choice)
    choice = change_choice(doors=doors, negative_door_not_choice=negative_door_not_choice, choice=choice, switch=switch)
    if choice == positive:
        return True
    else:
        return False


def main():
    tests_count = 10
    for _ in range(30):
        results = []

        for _ in range(tests_count):
            results.append(run(switch=True))

        positive = 0
        for result in results:
            if result:
                positive += 1

        print(positive / tests_count * 100)

        results.clear()
        positive = 0
        for _ in range(tests_count):
            results.append(run(switch=False))

        positive = 0
        for result in results:
            if result:
                positive += 1

        print(positive / tests_count * 100)


if __name__ == '__main__':
    main()