# tast 1.1

age=int(input("Enter the  yours age: "))
print("I'm "+str(age)+" years old")

# task 1.2

a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
print("the sum is: "+str(a+b))

# task 2.1

num=int(input("Enter the number: "))
print("Number is even") if num%2==0 else print("Number is odd")

# task 2.2

for i in range(1,6):
    print(i)

# task 3.1

def multiply(a,b):
    return (a*b)
print(multiply(-5.1,4))

# task 3.2

import math
num_for_sqrt=int(input("Enter the number: "))
print("SQRT for "+str(num_for_sqrt)+" number is: "+str(math.sqrt(num_for_sqrt)))

# task 4.1
f = open('data.txt', 'a')
f.write("\nAny text")
f.close()

# tas 4.2

f = open('data.txt', 'r')
print(f.read())
f.close()

#task 5.1

try:
    ex_num=int(input("Enter the number: "))
except ValueError:
    print("Only integers are allowed")
else:
    print("Okey")

#task 5.2

def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("We can't divide a number by 0")

division(3,0)