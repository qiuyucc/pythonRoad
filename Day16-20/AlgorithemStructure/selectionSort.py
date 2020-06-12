# selection sort

def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def selection_sort(origin_items):
    items = origin_items[:]
    for x in range(len(items) - 1):
        min_index = x
        for j in range(x + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[x], items[min_index] = items[min_index], items[x]
    return items

if __name__ == '__main__':
    list1 = [1, 23, 63, 12, 13, 53, 12, 31, 199, 22, 3, 5, 6]
    print(select_sort(list1))
    print(selection_sort(list1))

#
