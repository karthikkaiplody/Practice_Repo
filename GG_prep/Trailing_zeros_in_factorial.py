
def countZeros(N):
    sum_ = 0
    i = 5
    while (N/i >= 1):
        sum_ += int(N/i)
        i *= 5 
    return int(sum_)    
    

print(countZeros(384))