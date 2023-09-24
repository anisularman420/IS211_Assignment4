import time
import random


# Function to generate a random list of positive integers
def get_random_list(n):
    return [random.randint(1, 1000000) for _ in range(n)]


# Sequential Search
def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


# Ordered Sequential Search
def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


# Binary Search (Iterative)
def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


# Binary Search (Recursive)
def binary_search_recursive(a_list, item, first, last):
    if first > last:
        return False
    else:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search_recursive(a_list, item, first, midpoint - 1)
        else:
            return binary_search_recursive(a_list, item, midpoint + 1, last)


# Benchmarking function
def benchmark_search_algorithms(list_sizes, num_trials):
    for size in list_sizes:
        total_time_seq = 0
        total_time_ordered_seq = 0
        total_time_binary_iter = 0
        total_time_binary_rec = 0

        for _ in range(num_trials):
            random_list = get_random_list(size)
            random_list.sort()

            # Sequential Search
            start_time = time.time()
            sequential_search(random_list, -1)  # Search for an element that doesn't exist
            end_time = time.time()
            total_time_seq += (end_time - start_time)

            # Ordered Sequential Search
            start_time = time.time()
            ordered_sequential_search(random_list, -1)  # Search for an element that doesn't exist
            end_time = time.time()
            total_time_ordered_seq += (end_time - start_time)

            # Binary Search (Iterative)
            start_time = time.time()
            binary_search_iterative(random_list, -1)  # Search for an element that doesn't exist
            end_time = time.time()
            total_time_binary_iter += (end_time - start_time)

            # Binary Search (Recursive)
            start_time = time.time()
            binary_search_recursive(random_list, -1, 0,
                                    len(random_list) - 1)  # Search for an element that doesn't exist
            end_time = time.time()
            total_time_binary_rec += (end_time - start_time)

        avg_time_seq = total_time_seq / num_trials
        avg_time_ordered_seq = total_time_ordered_seq / num_trials
        avg_time_binary_iter = total_time_binary_iter / num_trials
        avg_time_binary_rec = total_time_binary_rec / num_trials

        print(f"List Size: {size}")
        print(f"Sequential Search took {avg_time_seq:.7f} seconds on average.")
        print(f"Ordered Sequential Search took {avg_time_ordered_seq:.7f} seconds on average.")
        print(f"Binary Search (Iterative) took {avg_time_binary_iter:.7f} seconds on average.")
        print(f"Binary Search (Recursive) took {avg_time_binary_rec:.7f} seconds on average.")
        print()


if __name__ == "__main__":
    list_sizes = [500, 1000, 10000]
    num_trials = 100
    benchmark_search_algorithms(list_sizes, num_trials)
