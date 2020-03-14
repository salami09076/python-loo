def step_by_one(drw_numbers):
    result_list = list()

    for i in range(1, 45):

        temp = list(map(lambda x: x + i, drw_numbers))

        # Single Expression
        step_list = list(map(lambda x: x > 45 and x - 45 or x, temp))

        # Ternary Operator
        # step_list = list(map(lambda x: x- 45 if x > 45 else x, temp))

        result_list.append(step_list)

    return result_list


if __name__ == "__main__":
    print(step_by_one((1, 2, 3, 4, 5, 6, 7, 8)))
