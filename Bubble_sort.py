def bubblesort(arr):
    n = len(arr)
    # Traverse through the entire array
    for i in range(n):
        # Separate the last maxed out element in each pass
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

#arr = [70,20,50,30,90,5,15]
arr = [100,6,20,78,101,35]
bubblesort(arr)
for i in range(len(arr)):
    print(arr[i])

