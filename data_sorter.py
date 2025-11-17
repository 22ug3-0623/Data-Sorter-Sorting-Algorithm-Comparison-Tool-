# --- Bubble Sort (22UG3-0623) ---
def bubble_sort(arr):
    """Sorts an array using Bubble Sort and tracks performance."""
    n = len(arr)
    perf = Performance("Bubble Sort")
    perf.data_size = n
    perf.start_timer()

    local_arr = list(arr) # Work on a copy

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            perf.increment_step(1) # Count comparison step
            if local_arr[j] > local_arr[j + 1]:
                # Swap operation
                local_arr[j], local_arr[j + 1] = local_arr[j + 1], local_arr[j]
                swapped = True

        # Optimization: if no two elements were swapped by inner loop, then break
        if not swapped:
            break

    perf.stop_timer()
    perf.sorted_list = local_arr
    return perf
