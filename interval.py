def get_interval(drw_numbers):

    result_list = list()

    # 첫 숫자 제외
    a = list(drw_numbers[i] - drw_numbers[i - 1] for i in range(1, 6))

    # 첫 숫자 포함
    b = list()
    for i in range(6):
        if i == 0:
            b.append(drw_numbers[i])
            continue
        b.append(drw_numbers[i] - drw_numbers[i - 1])

    # 첫 숫자 포함 (연산과 코드가 적은 버전)
    c = list(drw_numbers[i] - drw_numbers[i - 1] for i in range(1, 6))
    c.insert(0, drw_numbers[0])

    # 첫 숫자 포함 및 불포함 버전
    result_list.append(a)
    result_list.append(c)

    return result_list


if __name__ == '__main__':
    print(get_interval([5, 18, 20, 23, 30, 34, 21])) # 901회차 당첨번호
