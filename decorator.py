import time

#Create a decorator timer that prints the time taken by a function to execute.
def timer(func):

    def inner():
        start=time.time()
        time.sleep(2)
        func()
        end=time.time()
        print(end-start)

    return inner

@timer
def print_a():
    print("a")

#print_a()

#Write a decorator logger that logs the function name and its arguments when the function is called.

def logger(func):

    def inner(*args, **kwargs):
        print("Function name is:"+str(func.__name__))
        func(args,kwargs)
        print("arguments are :")
        for i in args:
            print(i)
        for key, value in kwargs.items():
            print(key, ":", value)

    return inner

@logger
def print_all(*args, **kwargs):
    pass

#print_all(1,"sf",85, a="bye")


#Implement a decorator memoize that memoizes the result of a function for given arguments.

def memorizes(func):
    memo={}
    def inner(*args,**kwargs):
        print("Result for: ")
        for i in args:
            print(i, end=', ')
        print(" arguments is: ")

        if args in memo:
            print(memo[args])
        else:
            print("New")
            result=func(*args,**kwargs)
            print(result)
            memo[args] = result

    return inner

@memorizes
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
