Link = "https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/"
Description = "I am using this to find all the prime number in a given range.We'll create a boolean array of range " \
              "up to n+1 with all the values initialized with True Where we find any number as a multiple of any " \
              "other number, we'll assign it as False. So at the end we'll be left with an array consisting True at " \
              "the position of prime numbers"
def SieveOfEratosthenes(n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False
    i = 2
    while i*i <= n: #We have to run the loop till root n times
        if arr[i] == False:
            pass
        else:
            for j in range(2*i,len(arr)):
                if j%i == 0:
                    arr[j] = False
        i+=1
    return arr
if __name__ == '__main__':
    n = 36
    arr = SieveOfEratosthenes(n)
    for i in range(1,len(arr)):
        mark = "Not Prime"
        if arr[i]:
            mark = "Prime"
        print(i , " is ",mark)