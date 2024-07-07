# Memoization
# Using Dictionary, Keys will be arg to the fn, value will be the retun value

def fib(n, memo = {}):
    # First we check if the value is in the dict
    if n in memo:
        return memo[n]
    # This is the base case
    if n <= 2:
        return 1
    # Since we'll have to calculate at least once. We are going to store the value in our dict
    memo[n] = fib(n - 1) + fib(n - 2)
    # Finally we return our value through dict
    return memo[n]