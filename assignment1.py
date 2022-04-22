print("QUESTION 1 :")
a = int(input("ENTER A NUMBER : "))
b = int(input("ENTER ANOTHER NUMBER : "))
c = int(input("ENTER ANOTHER NUMBER : "))
avg = (a + b + c)/3
print(avg)

#######################################################################

print("QUESTION 2 :")
gross_income = int(input("ENTER GROSS INCOME : "))
dependents = int(input("ENTER NUMBER OF DEPENDENTS : "))
taxable_inc = gross_income - 10000 - 3000*dependents
Tax = taxable_inc*0.2
print(Tax)

########################################################################

print("QUESTION 3 :")
sid = int(input("ENTER YOUR SID : "))
name = input("ENTER YOUR NAME : ")
gender = input("ENTER YOUR GENDER : ")
course_name = input("ENTER YOUR COURSE NAME : ")
'''SID, Name, Gender, Course_name in student'''
CGPA = float(input("ENTER YOUR CGPA"))
student = []
student.append(sid)
student.append(name)
student.append(gender)
student.append(course_name)
student.append(CGPA)
print(student)

########################################################################

print("QUESTION 4 :")
a = int(input("ENTER MARKS OF FIRST STUDENT " ))
b = int(input("ENTER MARKS OF SECOND STUDENT "))
c = int(input("ENTER MARKS OF THIRD STUDENT"))
d = int(input("ENTER MARKS OF FOURTH STUDENT "))
e = int(input("ENTER MARKS OF FIFTH STUDENT"))
marks = [a,b,c,d,e]
marks.sort()
print(marks)

#########################################################################

print("QUESTION 5 :")
Color = ["Red","Green","White","Black","Pink","Yellow"]
Color.pop(3)
print(Color)
Color[3] = "Purple"
print(Color)
