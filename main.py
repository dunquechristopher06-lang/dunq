def bubble_sort(arr):
    # Create a copy so the original unsorted array stays unchanged
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent letters alphabetically
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        # Stop early if the array is already sorted
        if not swapped:
            break

    return sorted_arr


def process_name(full_name):
    unsorted_array = []

    for char in full_name:
        # Exclude symbols, numbers, and spaces (only keep letters)
        if char.isalpha():
            # Standardize to uppercase so duplicates like 'R' and 'r' are caught
            letter = char.upper()

            # Discard duplicate letters
            if letter not in unsorted_array:
                unsorted_array.append(letter)

    return unsorted_array


# --- Main Program ---
full_name = "Christopher Dunque"

unsorted_letters = process_name(full_name)
sorted_letters = bubble_sort(unsorted_letters)

print(f"Full Name:      {full_name}")
print(f"Unsorted Array: {unsorted_letters}")
print(f"Sorted Array:   {sorted_letters}")  