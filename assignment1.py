# Name: Dominic Fantauzzo
# OSU Email: fantauzd@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1 - Python Fundamentals Review
# Due Date: 1/30/2024
# Description: Write a series of short python function using the static array data structure to
#              review python syntax constructs and begin analyzing Big-O notation while developing algorithms


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    Receives a one-dimensional array of integers and returns a Python
    tuple with two values - the minimum and maximum values of the input array.

    :param arr: an array of integers

    :return: a tuple with the minimum value at index 0 and the maximum value at index 1
    """
    # Initialize variables min and max to the first element of the array
    mini = arr[0]
    maxi = arr[0]
    # Check each element and reassign min or max if a smaller or greater element is found, respectively
    for num in range(arr.length()):
        if arr[num] < mini:
            mini = arr[num]
        if arr[num] > maxi:
            maxi = arr[num]

    result = (mini, maxi)
    return result

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray of integers and returns a new StaticArray object
    with the content of the original array modified so integers divisible by 3 return "fizz",
    integers divisible by 5 return "buzz", and integers that are both return "fizzbuzz".

    :param arr: an array of integers

    :return: a new StaticArray object of integers and strings
    """
    # Create a new static array of the same length
    # Assign each index, a string or the same value as the StaticArray argument
    newArr = StaticArray(arr.length())
    for num in range(arr.length()):
        if arr[num] % 3 == 0 and arr[num] % 5 == 0:
            newArr[num] = "fizzbuzz"
        elif arr[num] % 3 == 0:
            newArr[num] = "fizz"
        elif arr[num] % 5 == 0:
            newArr[num] = "buzz"
        else:
            newArr[num] = arr[num]
    # return the new, modified static array
    return newArr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Receives a StaticArray and reverses the order of the elements
    in the array in place.

    :param arr: an array

    :return: None
    """
    # Create a variable to store the mirrored opposite index and swap values from
    # the first half to the second half of the array, excluding median if length is odd
    last = arr.length()-1
    for num in range(arr.length()//2):
        temp = arr[num]
        arr[num] = arr[last]
        arr[last] = temp
        last -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Creates and returns a new StaticArray, which contains all the elements
    from the original array, but their position has shifted right or left steps number of times

    :param arr: a static array
    :param steps: an integer (positive for right rotation, negative for left rotation)

    :return: the rotated static array
    """
    # Find the number of real rotations we will perform, complete rotations have no effect
    realSteps = steps - int(steps/arr.length()) * arr.length()
    # if the rotation is negative (leftwards), find the number of rightward rotations that is equivalent
    if realSteps < 0:
        realSteps = arr.length() + realSteps

    newArr = StaticArray(arr.length())
    # iterate over each value in the array and assign it to its rotated position in the new array
    for num in range(arr.length()):
        if (num + realSteps) < (arr.length()):
            newArr[num + realSteps] = arr[num]
        else:
            newArr[(num + realSteps - arr.length())] = arr[num]

    return newArr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Receives the two integers start and end, and returns a StaticArray that
    contains all the consecutive integers between start and end (inclusive)

    :start: an integer
    :end: an integer

    :return: a static array
    """
    newArr = StaticArray(abs(end - start)+1)
    count = 0
    # assigns numbers to the new static array consecutively in positive or negative direction
    if end >= start:
        for num in range(start, end+1):
            newArr[count] = num
            count += 1
    else:
        for num in range(start, end-1, -1):
            newArr[count] = num
            count += 1

    return newArr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Receives a StaticArray and returns an integer that describes whether the array is sorted.
    (1: strictly ascending, -1: strictly descending, 0: other)

    :param arr: a static array

    :return: an int from -1 to 1 inclusive
    """
    des = False
    asc = False

    if arr.length() == 1:
        return 1
    # iterate over array and use variable to record if any consecutive values are descending/ascending
    for num in range(arr.length()-1):
        if arr[num] >= arr[num+1]:
            des = True
        if arr[num] <= arr[num+1]:
            asc = True
        # if we have values in both descending and ascending then order is other
        if des is True and asc is True:
            return 0
    if asc is True and des is False:
        return 1
    if des is True and asc is False:
        return -1
    # if we have values in both descending and ascending, or never ascending nor descending then order is other
    else:
        return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------


def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Receives a StaticArray that is sorted in either non-descending or
    non-ascending order. The function will return the mode (the most-occurring element) of the
    array and its frequency (how many times it appears) as a tuple.

    :param arr: a static array

    :return: a tuple like (mode, frequency)
    """
    # create variables to store the mode, mode frequency, and the current element and its frequency
    mode = arr[0]
    modeFreq = 0
    el = None
    elFreq = 0
    # Increment mode frequency or element frequency when we iterate over like elements.
    # When iterating over new elements, compare the frequency of the last element with mode
    # and update mode if appropriate.
    for num in range(arr.length()):
        if arr[num] == mode:
            modeFreq += 1
        elif arr[num] == el:
            elFreq += 1
        else:
            if elFreq > modeFreq:
                mode = el
                modeFreq = elFreq

            el = arr[num]
            elFreq = 1
    # perform final check to see if last element was mode
    if elFreq > modeFreq:
        mode = el
        modeFreq = elFreq

    return (mode, modeFreq)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray that is already in sorted order, either
    non-descending or non-ascending. The function will return a new StaticArray with all
    duplicate values removed.

    :param arr: a static array

    :return: a new static array
    """
    extra = 0
    # iterate over array to count the number of values in the array argument that are not unique
    for num in range(1, arr.length()):
        if arr[num] == arr[num-1]:
            extra += 1
    # create a new array with one space for each unique value
    newArr = StaticArray(arr.length()-extra)
    val = None
    pos = 0
    # iterate over the array and copy unique values to the new array
    for num in range(arr.length()):
        if arr[num] != val:
            newArr[pos] = arr[num]
            val = arr[num]
            pos += 1

    return newArr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray and returns a new StaticArray with the same content sorted in non-ascending order.

    :param arr: a static array

    :return: a new static array
    """
    # iterate through the array to find the min and max value.
    # then generate a static array with a size equal to the number of different possible values
    minMax = min_max(arr)
    min = minMax[0]
    max = minMax[1]
    countArr = sa_range(min, max)
    # initialize all values in count array to 0
    for num in range(countArr.length()):
        countArr[num] = 0
    # iterate over array argument to count how many times each value appears
    for num in range(arr.length()):
        countArr[abs(arr[num]-max)] += 1
    # modify count array to represent the ending index for each unique value by setting
    # subsequent values equal to count array + the previous value in count array.
    for num in range(1, countArr.length()):
        countArr[num] = countArr[num-1] + countArr[num]
    # create a new array to hold the final, sorted array
    newArr = StaticArray(arr.length())
    pos = 0
    # Handle the first unique value (max) by setting one index equal to the first unique value
    # for each appearance (count) in the original list
    for num in range(countArr[0]):
        newArr[pos] = max
        pos += 1
    max -= 1
    # Repeat the process for all other unique values, using the count array to get the starting and ending index
    # During each iteration of the innermost loop, we adjust position so a new index is set to the unique value for
    # each appearance. During each iteration of the outer loop, we decrement max to get the next unique value.
    for index in range(1,countArr.length()):
        for num in range(countArr[index-1],countArr[index]):
            newArr[pos] = max
            pos += 1
        max -= 1

    return newArr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray where the elements are in sorted order, and
    returns a new StaticArray with squares of the values from the original array, sorted in
    non-descending order.

    :param arr: a static array

    :return: a new static array
    """
    # the largest value will either be at the left or right position, so we create the squared
    # array by working from the outside in, putting the squared array in non-increasing order
    newArr = StaticArray(arr.length())
    left = 0
    right = arr.length() -1
    count = 0
    # iterates from outside (largest values) inwards (toward smaller values)
    # until we have gone through all values
    while left <= right:
        # finds the next largest value and assigns it to next position in the new array
        if abs(arr[left]) >= abs(arr[right]):
            newArr[count] = (arr[left])**2
            left += 1
            count += 1
        else:
            newArr[count] = (arr[right])**2
            right -= 1
            count += 1
    # we want to change the order from non-increasing to non-descending so we can use reverse
    reverse(newArr)

    return(newArr)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
