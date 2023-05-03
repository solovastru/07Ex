#Exercise 06

# recursive function
def power(a, b) -> int:

    if a <= 0 or b <= 0:
        return -1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)


result = power(2, 4)
print("Recursive power is", result)


# binary search

def binary_search(numbers, num, low, high):

    if low > high:
        return - 1

    else:
        mid = (low + high) // 2
        if num > numbers[mid]:
            return binary_search(numbers, num, mid + 1, high)
        elif num < numbers[mid]:
            return binary_search(numbers, num, low, mid - 1)
        else:
            return mid

numbers = [4, 6, 10, 15, 38, 45]
index = binary_search(numbers, 15, 0, len(numbers) - 1)
print("Index of 15:", index)

