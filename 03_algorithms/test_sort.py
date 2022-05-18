import my_sort.init_list as init
import my_sort.sorting as sort

n = 1000000
# list_ = init.random_list_dif_int(n)
list_ = [i for i in range(n, 0, -1)]
# list_ = [i for i in range(0, n, 1)]

sort.test_sort_func(sort.sort_merge, list_.copy())
sort.test_sort_func(sort.sort_merge, list_.copy())
sort.test_sort_func(sort.sort_merge, list_.copy())
# sort.test_sort_func(sort.sort_merge, list_.copy())
#
# sort.test_sort_func(sort.sort_insertion, list_.copy())
# sort.test_sort_func(sort.sort_insertion, list_.copy())
#
# sort.test_sort_func(sort.sort_selection, list_.copy())
# sort.test_sort_func(sort.sort_selection, list_.copy())
