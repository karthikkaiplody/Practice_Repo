class Median():
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2


    def median(self):
        print( self.arr1, self.arr2)
        arr3 = self.arr1 + self.arr2
        arr3 = sorted(arr3)
        if len(arr3) % 2 != 0:
            return arr3[int(len(arr3) / 2)]
        else:
            return (arr3[int(len(arr3) / 2)] + arr3[(int(len(arr3) / 2)) - 1]) / 2


result = Median(arr1, arr2)
print(result.median())