def bidirectional_ripple_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    start, end = 0, n - 1
    swapped = True

    while swapped:
        swapped = False
        # forward pass: push the largest to end
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        end -= 1

        swapped = False
        # backward pass: push the smallest to start
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

    return arr

# Example usage
if __name__ == "__main__":
    data = [5, 1, 4, 2, 8, 0, -1, 3]
    print("Original:", data)
    sorted_data = bidirectional_ripple_sort(data)
    print("Sorted  :", sorted_data)
    