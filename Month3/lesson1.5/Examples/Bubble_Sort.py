def bubble_sort(arr):
    """
    Bubble Sort Algorithm

    This function sorts a list of numbers in ascending order using the Bubble Sort technique.
    The algorithm works by repeatedly stepping through the list, comparing adjacent pairs of
    elements and swapping them if they are in the wrong order. This process is repeated until
    the list is sorted.

    Parameters:
        arr (list): The list of numbers to sort.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    # Outer loop: We need to perform n-1 passes in the worst-case scenario.
    for i in range(n):
        # swapped flag helps us to determine if any swap happened during this pass.
        # If no swaps occur, the list is already sorted.
        swapped = False

        # Inner loop: In each pass, the largest unsorted element "bubbles up" to its correct position.
        # The last i elements are already sorted after i passes, so we reduce the inner loop's range.
        for j in range(0, n - i - 1):
            # Compare the current element with the next element.
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True to indicate that a swap occurred.
                swapped = True

        # If no elements were swapped in the inner loop, then the list is sorted.
        if not swapped:
            break

    return arr

# Example usage:
if __name__ == "__main__":
    # Sample list to sort
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)
    sorted_list = bubble_sort(sample_list)
    print("Sorted list:", sorted_list)
