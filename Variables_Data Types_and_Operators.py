"""
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
"""
"""
Task: Write a Python script that does the following:

Creates a list of dictionaries, where each dictionary contains information about a student (name, age, and grades).
Calculates the average grade of all students.
Finds the student with the highest grade.
"""


studets=[
{"name": "Anna", "age": 20,"grades": 15},
{"name": "Paris", "age": 21,"grades": 17.5},
{"name": "Davit", "age": 18,"grades": 20}
]
s=0;
hg=studets[0]["grades"]
id=0
for i in studets:
    s+=i["grades"]
    if i["grades"]>hg:
        hg=i["grades"]
        id=studets.index(i)

print("The avg equalt: "+str(s/len(studets)))
print(f"The student id with  highest grade : {id} and grade is: {hg}")

"""
Task: Write a Python function that takes a list of integers and returns a new list containing only the even numbers. 
Use both a loop and a list comprehension to solve this.
"""

def even_num(numbers_list):
    return [num for num in  numbers_list if num%2==0 ]
def even_num(numbers_list):
    even_list=[]
    for number in numbers_list:
        if number%2==0:
            even_list.append(number)
    return even_list

"""
Task: Write a Python function that takes two arguments, a list of numbers and a target number, 
and returns a tuple containing two numbers from the list that add up to the target number. 
Assume there is exactly one solution.
"""
def sum_elem_optimized(num_list, target):
    seen = set()
    for num in num_list:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return "There are no pairs of numbers that sum to the target"

# Test the optimized function
print(sum_elem_optimized([1, 2, 3, 4, 5, 6, 5], 10))  # Output: (4, 6)
print(sum_elem_optimized([20], 20))  # Output: "There are no pairs of numbers that sum to the target"
print(sum_elem_optimized([], 10))  # Output: "There are no pairs of numbers that sum to the target"
print(sum_elem_optimized([1, 2, 3], 7))  # Output: "There are no pairs of numbers that sum to the target"
