""" move zeros project

used to separate 0s from the array  and move it to the end of the list
"""
def move_zeros(numbers):
    """
    :param numbers: a list of integers
    :return: the all numbers to the left side and 0s to the right side
    """
    count_zero = []
    others = []
    for i in range(len(numbers)):
        if numbers[i] != 0:
            others.append(numbers[i])
        else:
            count_zero.append(numbers[i])
    return others+count_zero

Numbers=[11,6,0,3,0,22,-1]
print(move_zeros(Numbers))
