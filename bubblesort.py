arr = [0,1,5,3,2,8]

def bubbleSort(arr):
    count = 0
    for j in range(len(arr)-1):
        # print("\n\n", "-"*50, "iteration", j)
        for i in range(len(arr)-1-j):
            count += 1
            # print("\n","*"*80, "\n", "index", i, "value", arr[i])
            # print("\n","*"*80, "\n", "comparing", arr[i], arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # print("swapped", arr[i], arr[i+1])
                # print("array is now", arr)
            # else:
            #     print("no need to swap", arr[i], arr[i+1])
    return arr
bubbleSort(arr)