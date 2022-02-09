def solution(arr):
    min = 1000000000;
    if(len(arr)-1):
        for i in range(len(arr)):
            if arr[i]<min:
                min=arr[i]
        arr.remove(min)
        return arr
    else:
        return [-1]