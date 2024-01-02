import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr


ten_elements = []
for _ in range(10):
    num = random.random()
    ten_elements.append(num)

twenty_elements = []
for _ in range(20):
    num = random.random()
    twenty_elements.append(num)

hundred_elements = []
for _ in range(100):
    num = random.random()
    hundred_elements.append(num)

two_hundred_elements = []
for _ in range(200):
    num = random.random()
    two_hundred_elements.append(num)


# merge_sort()
print('merge_sort() for 10: {} sec'.format(round(timeit.timeit('[merge_sort(ten_elements)]', number=1, globals=globals()), 5)))
print('merge_sort() for 20: {} sec'.format(round(timeit.timeit('[merge_sort(twenty_elements)]', number=1, globals=globals()), 5)))
print('merge_sort() for 100: {} sec'.format(round(timeit.timeit('[merge_sort(hundred_elements)]', number=1, globals=globals()), 5)))
print('merge_sort() for 200: {} sec'.format(round(timeit.timeit('[merge_sort(two_hundred_elements)]', number=1, globals=globals()), 5)))

# insertion_sort()
print('insertion_sort() for 10: {} sec'.format(round(timeit.timeit('[insertion_sort(ten_elements)]', number=1, globals=globals()), 6)))
print('insertion_sort() for 20: {} sec'.format(round(timeit.timeit('[insertion_sort(twenty_elements)]', number=1, globals=globals()), 6)))
print('insertion_sort() for 100: {} sec'.format(round(timeit.timeit('[insertion_sort(hundred_elements)]', number=1, globals=globals()), 6)))
print('insertion_sort() for 200: {} sec'.format(round(timeit.timeit('[insertion_sort(two_hundred_elements)]', number=1, globals=globals()), 6)))

# merge()
print('Sorted() for 10: {} sec'.format(round(timeit.timeit('[sorted(ten_elements)]', number=1, globals=globals()), 7)))
print('Sorted() for 20: {} sec'.format(round(timeit.timeit('[sorted(twenty_elements)]', number=1, globals=globals()), 7)))
print('Sorted() for 100: {} sec'.format(round(timeit.timeit('[sorted(hundred_elements)]', number=1, globals=globals()), 7)))
print('Sorted() for 200: {} sec'.format(round(timeit.timeit('[sorted(two_hundred_elements)]', number=1, globals=globals()), 7)))
