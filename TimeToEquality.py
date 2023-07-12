def TimeToEquality(array):
    array.sort()
    end = array[-1]
    time = 0
    
    for i in range(len(array)-1):
        time += end - array[i]
    return time

array = list(map(int,input().strip().split()))
print(TimeToEquality(array))