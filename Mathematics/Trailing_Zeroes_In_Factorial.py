def trailingZeroes(n):
    res = 0
    i = 5
    while i <= n:
        res+= n//i
        i*=5
    return res
n = 30
print("Number of Zeros in factorial of {0} is ".format(n),trailingZeroes(n))