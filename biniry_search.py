def biniry_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        guses = list[mid]
        if guses == item:
            return mid
        if guses > item:
            hight = mid -1
        else:
            low = mid + 1

    return None

test_list = [ 4, 8, 9, 11, 13, 15, 17, 19, 20, 25]

print(biniry_search(test_list, 25))