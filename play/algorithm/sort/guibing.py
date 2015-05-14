__author__ = 'Administrator'
from sort import *

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq)/2)
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == '__main__':
    t = rand_list(100000)
    print(t)
    print(merge_sort(t))

