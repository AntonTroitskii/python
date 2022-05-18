import random

FILE_NAME = 'random.list.txt'
FILE_NAME_10 = 'random.list.10.txt'
FILE_NAME_100 = 'random.list.100.txt'
FILE_NAME_1000 = 'random.list.1000.txt'


def create_unsorted_list_in_file(n=30):
    init_list = random_list_rand_int(n)

    file_obj = open(FILE_NAME, 'w')
    file_obj.writelines(digit + ' ' for digit in map(str, init_list))
    file_obj.close()


def random_list_rand_int(n):
    init_list = []
    k = n - 1
    for i in range(0, n):
        init_list.append(random.randint(0, k))
    return init_list


def random_list_dif_int(n):
    init_list = []
    for i in range(0, n):
        init_list.append(i)
    # randomize
    for i in range(0, n):
        i1 = random.randint(0, n - 1)
        i2 = random.randint(0, n - 1)

        init_list[i1], init_list[i2] = init_list[i2], init_list[i1]
    return init_list


def read_list(file=FILE_NAME):
    file_obj = open(file, 'r')
    res = list(map(int, file_obj.readline().split()))

    return res
