from time import time


def bubble_sort(origin_items):
    start = time()
    items = origin_items[:]
    for x in range(len(items) - 1):
        for i in range(len(items) - 1 - x):
            if items[i] > items[i + 1]:
                temp = items[i + 1]
                items[i + 1] = items[i]
                items[i] = temp
    end = time()
    result = end - start
    print(f'cocktail sort: {result}')
    return items


# improved bubble_sort [cocktail sort]

def cocktail_sort(origin_items, comp=lambda x, y: x < y):
    '''高质量冒泡排序（鸡尾酒）'''
    start = time()
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        # 如果一个回合里面没有发生swapped， 那就说明排序已完成，不用再比较
        if not swapped:
            break
    end = time()
    result = end - start
    print(f'cocktail sort: {result}')
    return items


if __name__ == '__main__':
    list1 = [1, 23, 63, 12, 13, 53, 12, 31, 199, 22, 3, 5, 6,]
    print(bubble_sort(list1))
    print(cocktail_sort(list1))
