def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where target is found
    return -1  # Not found

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found

if __name__ == "__main__":
    # Take array input from the user
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    
    target = int(input("Enter the number to search: "))

    print("\nChoose Search Method:")
    print("1. Linear Search")
    print("2. Binary Search")

    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        print("\nPerforming Linear Search...")
        result_linear = linear_search(arr, target)
        if result_linear != -1:
            print(f"Linear Search: Element found at index {result_linear}")
        else:
            print("Linear Search: Element not found")
    
    elif choice == 2:
        print("\nPerforming Binary Search (on sorted array)...")
        sorted_arr = sorted(arr)
        print(f"Sorted Array: {sorted_arr}")
        result_binary = binary_search(sorted_arr, target)
        if result_binary != -1:
            print(f"Binary Search: Element found at index {result_binary}")
        else:
            print("Binary Search: Element not found")
    
    else:
        print("Invalid choice! Please select either 1 or 2.")
