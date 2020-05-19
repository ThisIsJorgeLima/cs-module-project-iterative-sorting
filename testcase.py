import unittest

# sort them first
# run time


def find_repeat(numbers):
    numbers.sort()  # 0(nlogn)
    print(numbers)

    # we go through every value so its #0(n) for i in range....
    for i in range(len(numbers)):
        if numbers[i] is numbers[i+1]:
            return numbers[i]
# final runtime 0(nlogn) when you sort.
#
    return
