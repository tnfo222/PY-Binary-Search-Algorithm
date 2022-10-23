# code your iterative algorithm here

def binary_search (data, e1):
    first = 0
    last = len(data) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if data[mid] == e1:
            found = True
        else:
            if e1 < data[mid]:
                last = mid + 1
            else:
                first = mid + 1
    return found

test_list = [5,8,12,14,19,22,27,30,31]

print(binary_search(test_list,100)) 