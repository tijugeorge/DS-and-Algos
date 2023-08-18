def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)


####################################
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

memo = {}

#######################################

def fibonacci(n):
    arr = [0] * (n + 1)
    # base case - the second Fibonacci number is 1
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n]
