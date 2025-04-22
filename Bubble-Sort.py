def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        #We use this flag for Early exit if there are no Swaps
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == "__main__":
    #arr = [6, 3, 5, 1, 2, 10, 9]
    arr=list(map(int, input("Enter elements of array separated by spaces ").split()))

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
