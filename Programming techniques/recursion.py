import time

def fibIt(n):
    fibNumbers = [0, 1]
    for i in range(2, n):
        fibNumbers.append(fibNumbers[i - 1] + fibNumbers[i - 2])
    #end for
    return fibNumbers[n - 1]
#end function

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    #end if
#end function

startTime = time.time()
fib(10)
print("Recursive fib(10): ", time.time() - startTime)

startTime = time.time()

fibIt(10)
print("Iterative fib(10): ", time.time() - startTime)


startTime = time.time()
fib(30)
print("Recursive fib(30): ", time.time() - startTime)

startTime = time.time()

fibIt(30)
print("Iterative fib(30): ", time.time() - startTime)