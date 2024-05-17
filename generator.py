# Write a generator function count_up_to(n) that generates numbers from 1 to n.

def count_up_to(n):
    for i in range(1, n + 1):
        yield i


# Create a generator infinite_count(start) that starts counting from start and generates numbers infinitely.

def infinite_count(start):
    while True:
        yield start
        start += 1


# Implement a generator fibonacci() that generates an infinite sequence of Fibonacci numbers.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#Create a generator primes() that generates an infinite sequence of prime numbers.
import math

def primes():
    yield 2
    i=3
    while True:
        flag=0
        for j in range(3,int(math.sqrt(i))+1):
            if i%j==0:
                flag=1
                break
        if flag==0:
            yield i
        i+=2

