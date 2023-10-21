# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

def sockMerchant(n , ar):
    socks = dict()
    count = 0

    for i in ar: 
        if i in socks: 
            socks[i] += 1 
        else: 
            socks[i] = 1 
    
    for i in socks.values(): 
        count += i // 2
    
    return count

# Test cases
n  = 7
ar = [1, 2, 1, 2, 1, 3, 2]
print(sockMerchant(n, ar))

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))
