# Given a 6 x 6 2D Array, arr:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6 x 6.

def hourGlassSum(arr):
    maxSum = -99999999 

    for indxRow, row in enumerate(arr):
        for indxCol in range(len(row)): 
            if indxRow + 2 < len(arr) and indxCol + 2 < len(row): 
                curSum = sum(row[indxCol: indxCol + 3]) + arr[indxRow + 1][indxCol + 1] + sum(arr[indxRow + 2][indxCol: indxCol + 3])
                if curSum > maxSum:
                    maxSum = curSum

    return maxSum

# Test cases
arr = [[-9, -9, -9,  1, 1, 1], 
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]]

print(hourGlassSum(arr))

arr = [[-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]]
print(hourGlassSum(arr))
