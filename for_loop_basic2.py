
def biggieSize(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

print(biggieSize([-1,3,5,-5]))

def countPositives(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr

print(countPositives([-1,1,1,1]))

def sumTotal(arr):
    count = 0
    for i in range(0, len(arr)):
        count = count + arr[i]
    return count

print(sumTotal([1,2,3,4]))

def average(arr):
    avg = 0
    for i in range(0, len(arr)):
        avg = avg + arr[i]
    avg = avg / len(arr)
    return avg

print(average([1,2,3,4]))

def length(arr):
    print(len(arr))

length([1,2,3,4])

def minimum(arr):
    min = arr[0]
    if len(arr) < 1:
        return False
    else:
        for i in range(0, len(arr)):
            if arr[i] < min:
                min = arr[i]
    return min

print(minimum([1,2,3]))
print(minimum([-1,-2,-3]))

def maximum(arr):
    max = arr[0]
    if len(arr) < 1:
        return False
    else:
        for i in range(0, len(arr)):
            if arr[i] > max:
                max = arr[i]
    return max

print(maximum([1,2,3,4]))
print(maximum([-1,-2,-3]))

def ultimateAnalyze(arr):
    mydictionary = {"sumTotal": 0, "new_max": arr[0], "new_min": arr[0], "avg": 0}
    if len(arr) < 1:
        return False
    else:
        for i in range(0, len(arr)):
            if arr[i] < mydictionary["new_min"]:
                mydictionary["new_min"] = arr[i]
            if arr[i] > mydictionary["new_max"]:
                mydictionary["new_max"] = arr[i]
            mydictionary["sumTotal"] = mydictionary["sumTotal"] + arr[i]
    mydictionary["avg"] = mydictionary["sumTotal"] / len(arr)
    return mydictionary

print(ultimateAnalyze([1,2,3,4,5,6,7,8,9,10]))


def reverseList(arr):
    num = 0
    for i in range(len(arr)//2, -1, -1):
        num = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = num
    return arr

print(reverseList([1,2,3,4]))

# import math
# length = math.floor(len(arr)/2)











