import random


def get_random_number():
    # temp = set()

    # while len(temp) < 6:
    #     temp.add(random.randrange(1, 46))

    temp = random.sample(range(1, 46), 6)

    result_list = sorted(list(temp))

    return result_list


if __name__ == '__main__':
    print(get_random_number())
