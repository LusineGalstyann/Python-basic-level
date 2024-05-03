
#Write a Python function that takes a list of integers as input and returns the sum of all even numbers in the list.

def foo(l):
    l=iter(l)
    sum=0
    for i in l:
        if i%2==0:
            sum+=i
    return sum

print(foo( [1, 2, 3, 4, 5, 6]))


#Write a Python function that takes a list of strings as input and returns a new list containing the lengths of those strings.

def foo1(l):
    l=iter(l)
    a=[len(i) for i in l]
    return a
print(foo1( ["apple", "banana", "orange"]))

#Write a Python function that takes a list of numbers as input and returns a new list containing only
# the prime numbers from the original list
import math
def foo2(l):
    def isprime(num):
        flag=1
        if num==2: return True
        if num%2==1:
            for i in range(3,int(math.sqrt(num)),2):
                if num%i==0:
                    flag=0
                    return False
            if flag==1:
                return True
        else:
            return False


    l=iter(l)
    a=[i for i in l if isprime(i)]
    return a

print(foo2( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



