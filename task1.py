def combinations(lst: list, n: int) -> list:
    new_lst = list()
    if not n:
        return [[]]
    for i in range(len(lst)):
        curr = lst[i]
        remain_lst = lst[i+1:]

        remain_lst_comb = combinations(remain_lst, n-1)
        for el in remain_lst_comb:
            new_lst.append([curr, *el])
    return new_lst


def multiplicate(lst: list) -> list:
    comb_lst = list()
    for i in range(2, len(lst)+1):
        comb_lst += combinations(lst, i)

    prod_lst = list()
    for el in comb_lst:
        num = 1
        for i in el:
            num = num*i
        prod_lst.append(num)
    return sorted(list(set(prod_lst) - set(lst)), reverse=True)


if __name__ == '__main__':
    lst = [2, 3, 4, 5]
    print(multiplicate(lst))
