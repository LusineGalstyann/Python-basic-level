class Student():
    def __init__(self,name,age,grades):
        self.name=name
        if age in range(15,50):
            self.age=age
        else:
            raise ValueError("invalid argument!")
        self.grades=grades

    def add_grade(self,new_grade):
        if isinstance(new_grade,int, float) and new_grade in range(0,101):
            self.grades.append(new_grade)
        else:
            return ("Input wrong value")
    def avg_grade(self):
        if len(self.grades)==0:
            return("Student havent any grade")
        return sum(self.grades)/len(self.grades)
    def __str__(self):
        return (f"Studet's name is: {self.name} he/she is {self.age} years old and he have this grades: {self.grades}")
    def delete_grade(self,dg):
        if (dg in self.grades):
            self.grades.remove(dg)

student1 = Student("Anna", 20, [15, 18, 20])
print(student1)
print(student1.add_grade(19))
print(student1.avg_grade())
print(student1)

print(student1.add_grade("A"))

student1.delete_grade(18)
print(student1)

print(student1.delete_grade(100))