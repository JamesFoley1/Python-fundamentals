def countdown(num):
    count = []
    for i in range(num, -1, -1):
        count.extend([i])
    return count

print(countdown(5))

def printReturn(arr):
    print(arr[0])
    return arr[1]

def firstPlusLength(arr):
    count = arr[0]+len(arr)
    print(count)

firstPlusLength([0,1,2,3,4,5])

def greaterThanSecond(arr):
    newarr = []
    if len(arr) <= 1:
        return False
    else:
        for i in range(0, len(arr)):
            if arr[i] > arr[1]:
                newarr.extend([i])
        print(len(newarr), newarr)
    return newarr

greaterThanSecond([0,1,2,3,4,5])


def thisLengthThatValue(num1, num2):
    arr = []
    for i in range(0, num1):
        arr.extend([num2])
    if len(arr) == num2:
        print("Jinx!")
    return len(arr)
    
print(thisLengthThatValue(4,4))