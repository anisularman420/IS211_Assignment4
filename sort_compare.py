import random
import time


def get_me_random_list(n):
    """Generate a list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    """Implementation of insertion sort"""
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def shellSort(alist):
    """Implementation of shell sort"""
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    """Use Python's built-in sorted function"""
    return sorted(a_list)


if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        total_time = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)

            # Measure Python sort time
            start = time.time()
            sorted_list = python_sort(mylist.copy())
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Python sort took {avg_time:.7f} seconds on average for a list of {the_size} elements")

        total_time = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)

            # Measure insertion sort time
            start = time.time()
            insertion_sort(mylist.copy())
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Insertion sort took {avg_time:.7f} seconds on average for a list of {the_size} elements")
