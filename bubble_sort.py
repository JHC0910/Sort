#bubble sort

def bubbleSort(arr,order):
    max = len(arr)
    for i in range(1, max):
        j = 0
        while j < max-i:
            if((arr[j]>arr[j+1]) and (int(order)>0)) or ((arr[j]<arr[j+1]) and (int(order)<0)):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1
    return arr


A = [64, 25, 82, 22, 71, 93, 24, 55, 120, 9, 69] 
print('sorted_inverse:', bubbleSort(A, -1))
print('sorted_normal:', bubbleSort(A, 1))


