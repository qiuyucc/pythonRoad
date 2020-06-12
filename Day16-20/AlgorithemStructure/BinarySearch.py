def bin_search(items, key):
    '''binary search'''
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (end + start) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

