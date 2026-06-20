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

packets = [5005, 5001, 5009, 5003, 5008, 5002]

packets.sort()

target = 5008

result = binary_search(packets, target)

if result != -1:
    print("Packet Found at Index:", result)
else:
    print("Packet Not Found")
