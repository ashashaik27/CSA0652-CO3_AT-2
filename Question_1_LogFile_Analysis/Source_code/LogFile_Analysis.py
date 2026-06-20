def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

logs = [105, 101, 109, 103, 108, 102]

logs.sort()

target = 108

result = binary_search(logs, target)

if result != -1:
    print("Event Found at Index:", result)
else:
    print("Event Not Found")
