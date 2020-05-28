def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)

    # lenth of list
    print(len(list1))
    print(len(list2))

    # index of list
    print(list1[0])
    print(list1[4])
    print(list1[-1])
    print(list1[-3])
    # assign new value to list
    list1[2] = 300
    print(list1)
    # add element
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
    print(list1)
    print(len(list1))
    # delete element
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)

    # clean out list
    list1.clear()
    print(list1)


if __name__ == '__main__':
    main()
