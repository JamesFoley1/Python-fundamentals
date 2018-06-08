
def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1 , -1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                print(arr)
                print("\n",i, j)
    return arr

print(insertionSort([6,5,3,1,8,7,2,4]))