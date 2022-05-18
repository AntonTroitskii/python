import time


def test_sort_func(func, list_):
    if len(list_) < 1000:
        print(list_)

    start = time.clock()
    func(list_)
    end = time.clock()

    if len(list_) < 1000:
        print(list_)

    print('{}'.format(end - start))

    return list_


def sort_insertion(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while (i >= 0) and (a[i] > key):  # for i in range(j - 1, -1, -1):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


def sort_insetion_reverse(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while (i >= 0) and (a[i] < key):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


def sort_selection(a):
    n = len(a)
    for i in range(0, n - 1):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]


def sort_merge(a):
    # with flags
    # def merge(a_, p, q, r):
    #     left = a_[p: q+1]
    #     left.append(float('Infinity'))
    #     right = a_[q + 1: r + 1]
    #     right.append(float('Infinity'))
    #     i = 0
    #     j = 0
    #     for k in range(p, r+1):
    #         if left[i] <= right[j]:
    #             a_[k] = left[i]
    #             i += 1
    #         else:
    #             a_[k] = right[j]
    #             j += 1

    # without flag
    def merge(a_, p, q, r):
        left = a_[p: q + 1]
        # left.append(float('Infinity'))
        right = a_[q + 1: r + 1]
        # right.append(float('Infinity'))
        i = 0
        j = 0
        for k in range(p, r + 1):
            if left[i] <= right[j]:
                a_[k] = left[i]
                i += 1
                if i == len(left):
                    a_[k + 1: k + 1 + len(right[j:])] = right[j:]
                    return
            else:
                a_[k] = right[j]
                j += 1
                if j == len(right):
                    a_[k + 1: k + 1 + len(left[i:])] = left[i:]
                    return

    def merge_sort(a_, p, r):
        import math
        if p < r:
            q = math.trunc((p + r) / 2)
            merge_sort(a_, p, q)
            merge_sort(a_, q + 1, r)
            merge(a_, p, q, r)

    merge_sort(a, 0, len(a) - 1)
