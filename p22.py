def selection_sort(arr):
    n = len(arr) 
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Main Block
if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    print("\nChoose Sorting Method:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Bubble Sort")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        print("\nPerforming Selection Sort...")
        sorted_arr = selection_sort(arr)
        print("Sorted Array:", sorted_arr)

    elif choice == 2:
        print("\nPerforming Insertion Sort...")
        sorted_arr = insertion_sort(arr.copy())
        print("Sorted Array:", sorted_arr)

    elif choice == 3:
        print("\nPerforming Bubble Sort...")
        sorted_arr = bubble_sort(arr.copy())
        print("Sorted Array:", sorted_arr)

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
