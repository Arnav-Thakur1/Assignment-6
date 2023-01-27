class Student:
    pass

class Marks:
    pass

Marks_of_Arnav=Student()

marks_of_Arnav=Marks()

print("Arnav is an instance of class Student:",isinstance(Marks_of_Arnav,Student))
print("Arnav is an instance of class Marks:",isinstance(Marks_of_Arnav,Marks))
print("marks_of_Arnav is an instance of class Student:",isinstance(marks_of_Arnav,Student))
print("marks_of_Arnav is an instance of class Marks:",isinstance(marks_of_Arnav,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))