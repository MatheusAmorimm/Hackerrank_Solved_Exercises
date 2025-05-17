def plusMinus(arr):
    size = n #We have access to "n" in the problem
    
    numP = 0
    numN = 0
    zeros = 0
    
    for num in arr:
        if num > 0:
            numP += 1
        elif num < 0:
            numN += 1
        elif num == 0:
            zeros += 1
    print(f"{numP/size:.6f}\n{numN/size:.6f}\n{zeros/size:.6f}")
