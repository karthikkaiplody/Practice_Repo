"""
Array pair sum
Given an integer array, output all the unique pairs that sum up to a specific value k.
Input: pair_sum([1,2,3,2],4)
Output: (1,3)
        (2,2)
"""

"""
def pairsum(array, key):
    found = []
    output = []
    if len(array) < 1:
        return False
    for i in array:
        check = key - i
        if check in array and check not in found:
            found.append(check)
            output.append([i, check])

    return output


print(pairsum([1, 2, 3, 2], 4))

Author: Karthik
"""


def pair_sum(array, k):
    if len(array) < 2:
        return print("Array is too small")

    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print("\n".join(map(str, list(output))))


pair_sum([1, 2, 3, 2], 4)

# Author: FreeCodeCamp
