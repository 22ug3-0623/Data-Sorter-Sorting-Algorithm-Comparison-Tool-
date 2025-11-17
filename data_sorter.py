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
    
# ... (Merge Sort section placeholder/implementation by M2 goes here)
# --- Quick Sort  ---
def quick_sort(arr):
    """Sorts an array using Quick Sort and tracks performance."""
    perf = Performance("Quick Sort")
    perf.data_size = len(arr)
    
    # Use a mutable list to track steps across recursive calls
    step_count_list = [0] 
    local_arr = list(arr) 

    perf.start_timer()
    _quick_sort_recursive(local_arr, 0, len(local_arr) - 1, step_count_list)
    perf.stop_timer()
    
    perf.steps = step_count_list[0]
    perf.sorted_list = local_arr
    return perf

def _quick_sort_recursive(items, low, high, step_counter):
    if low < high:
        # Partition the array
        pivot_index, partition_steps = _partition(items, low, high)
        step_counter[0] += partition_steps
        
        # Recursive calls
        _quick_sort_recursive(items, low, pivot_index - 1, step_counter)
        _quick_sort_recursive(items, pivot_index + 1, high, step_counter)

def _partition(items, low, high):
    """Helper function to partition the array (Lomuto partition scheme)."""
    pivot = items[high]
    i = low - 1
    partition_steps = 0

    for j in range(low, high):
        partition_steps += 1 # Comparison step
        if items[j] <= pivot:
            i += 1
            # Swap items[i] and items[j]
            items[i], items[j] = items[j], items[i]
    
    # Swap items[i+1] and items[high] (the pivot)
    items[i + 1], items[high] = items[high], items[i + 1] 
    return i + 1, partition_steps

# --- 4. DISPLAY AND COMPARISON (Member 2's Final Task) ---
# ... (rest of the file)
