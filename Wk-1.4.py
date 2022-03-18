*/

Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given format.

	Write a program to perform various operations on tuples such as adding tuple, replacing tuple, slicing tuple and deleting tuple

/*


class Student:
     school = 'Sample_School'
     address = 'ABC, India'
 
student1 = Student()
student2 = Student()
student1.student_id = "21MCA2604"
student1.student_name = "Devansh Pandey"
student2.student_id = "PH04"
student2.marks_language = 75
student2.marks_science = 85
student2.marks_math = 71
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')

***************************************************************************************************************************************************

tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
# adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)

# repalcing with use of list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Accessing tuple elements using slicing
my_tuple = ('D', 'E', 'V', 'A', 'N', 'S', 'H', 'P', 'A')

# elements 2nd to 4th
print(my_tuple[1:4])

# elements beginning to 2nd
print(my_tuple[:-7])

# elements 8th to end
print(my_tuple[7:])

# elements beginning to end
print(my_tuple[:])

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)



