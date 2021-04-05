Link = "https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/"
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
a = 10
b = 30
print(gcd(a,b))