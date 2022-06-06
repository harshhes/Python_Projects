# Finding the nth Fibonacci no.
def fibonacci(n):
    (n-1) + (n-2)
    if (n<2):    # the base case i.e we know, fibonacci(0)=0, fibonacci(1)=1
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(9))
