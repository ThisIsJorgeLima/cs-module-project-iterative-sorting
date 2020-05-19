
# 0(n) time, 0(1) space


def o_1_space(n):
    total = 0  # 0(1)

    # range returns a 'range'
    # does the range obj utilize a constant amount of space?
    # range takes up a contant amount of space
    for i in range(n):  # 0(1) space
        total += i  # 0(1)

    return total


# 0(n) time, 0(n) space


# def o_n_space(n):
#     sums = []
#
#     for i in range(n):
#         sums.append(i+i)  # 0(n)
#
#     returns sums

# 0(n^2) time, 0(n^2) space


def _on2_space(n):
    times_table = []

    for j in range(n):  # 0(n) time loop
        row = []
        row.append(j * i)  # here we are adding n elements to the 'row' list
    times_table.append(row)  # now we have n lists that each hold n elements
    return times_table  # 0(n^2)

# space complexity cares about how much _additional_ space is being used
# 0(1) space
# don't count data structures that are passed in as input


def foo(arr):
    for x in arr:
        print(x + x)


# 0(n) space
def bar(arr):
    output = []

    for n in arr:
        output.append(n * n)  # 0(n) space is

    return output

# arr is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 0(n)


def baz(arr):
    evens = []

    # we're adding half of the values from the input array
    for n in arr:
        if n % 2 == 0:
            evens.append(n)  # 0(n / 2) == 0(1/2 * n) ~ 0(n) space

    return evens

# Pass by reference: the function is receiving a pointer to the input
# Pass by value: the function is receiving a copy of the input 0(n)

# 0(n^2) space


def o_2_space_v2(n):
    times_table = []

    for i in range(n):
        times_table.append(i)

        for j in range(n):
            times_table.append(j)

        return times_table

# space complexity cares about how much _additional_ space is being used space
