__author__ = 'egor'

#Given: A positive integer n≤25.

#Return: The value of Fn.

def fibo(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


def coolfibo(n):
    import math
    if isinstance(n,int):
        return round((pow((1+math.sqrt(5))/2,n)-pow((1-math.sqrt(5))/2,n))/math.sqrt(5))
    else:
        return "n is not an integer"

# Напишите декоратор для функции Fibonacci из предыдущего вопроса, который бы запоминал результаты вычислений. И при
# повторном вызове возвращал сохраненный результат.

def memoize(f):
    cache= {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf

@memoize
def Fibonacci(n):
    if n in [0, 1]:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)