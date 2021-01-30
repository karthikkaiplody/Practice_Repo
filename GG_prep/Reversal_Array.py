def arrayReversal(start, end):
    while(start<end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


n = int(input("Size of an array\n"))
arr = []
for i in range(n):
    element = int(input('Enter the element {}\n'.format(i)))
    arr.append(element)

print(arr)
arrayReversal(0, n-1)
print(arr)    