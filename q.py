def item(list01):
    list02 = []

    list02 = [item01 for item01 in list01 if item01 != 0]


    list02 += [0] * list01.count(0)

    return list02

    #     else:
    #         list02.append(item01)
    # for item02 in range(count):
    #     list02.append(0)
    #
    # return list02


print(item([1, 0, 0, 2, 0, 0, 0, 0, 5, 3]))