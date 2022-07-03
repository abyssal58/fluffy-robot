print(" Question 1 ")

n=int(input("Enter a number to find if it is a perfect number or not : "))
check=0
for i in range(1,int(n/2)+1):
    if(n%i==0):
        check=check+i
if(n==check):
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")
    

##################################################################################################

print(" Question 2 ")

str=input("Enter a word to check whether it is palindrome or not : ")
str_rev=str[::-1]
if(str==str_rev):
    print("The word is palindrome.")
else:
    print("The word is not palindrome.")


##################################################################################################


print(" Question 3 ")

list=[1]
space="  "
rows=int(input("Enter the number of rows : "))
for i in range(rows):
    space=space+"   "
a=[]
for i in range(rows):
    a=[]  
    for k in list:
        a.append(k)
    print(space,list)
    for j in range(1,len(list)):
        list[j]=a[j-1]+a[j]
    list.append(1)
    space=space[:-2]


##################################################################################################


print(" Question 4 ")

sen=input("Enter the sentence to check whether it is pangram or not: ")
a=97
A=65
count=0
for i in range(1,27):
    for i in range(0,len(sen)):
        if(sen[i]==chr(a) or sen[i]==chr(A)):
            count+=1
            break
    a=a+1
    A=A+1
if(count==26):
    print("The sentence is panagram.")
else:
    print("The sentence is not panagram.")
    
    
##################################################################################################


print(" Question 5 ")

str=input("Enter the string with hyphen separated sequence to arrange it in alphabetical order : ")
words=str.split("-")
words=sorted(words)
for i in words:
    print(i,"\b-",end="")
print("\b ")


##################################################################################################


print(" Question 6 ")

def student_data(student_name="N.A.",student_class="N.A"):
    global student_id
    print("### Data Print ###")
    print("Student ID : ",student_id)
    if(student_name!="N.A."):
        print("Student Name : ",student_name)
    if(student_class!="N.A."):
        print("Student Class : ",student_class)
student_id=input("Enter the Student ID : ")
cond=input("If you want to enter only student name then press n, only student class then c or both then b : ")
if(cond=="n"):
    s_name=input("Enter the Student's Name : ")
    student_data(s_name)
elif(cond=="c"):
    s_class=input("Enter the Student's class : ")
    student_data(s_class)
elif(cond=="b"):
    s_name=input("Enter the Student's Name : ")
    s_class=input("Enter the Student's class : ")
    student_data(s_name,s_class)
else:
    student_data()


##################################################################################################


print(" Question 7 ")

class student():
    pass
class Marks():
    pass
student_1=student()
Marks_1=Marks()
print("The instance student_1 is a instance of class student : ",isinstance(student_1,student))
print("The instance student_1 is a instance of class Marks : ",isinstance(student_1,Marks))
print("The instance Marks_1 is a instance of class student : ",isinstance(Marks_1,student))
print("The instance Marks_1 is a instance of class Marks : ",isinstance(Marks_1,Marks))
print("The class student is a sub-class of of the built in object class : ",issubclass(student,object))
print("The class Marks is a sub-class of of the built in object class : ",issubclass(Marks,object))


##################################################################################################


print(" Question 8 ")

class sum():
    def __init__(self,list):
        self.list=list
    def py_1(self):
        l1=len(self.list)
        print(self.list)
        sum_list=[]
        for i in range(0,l1-2):
            for j in range(i+1,l1-1):
                for k in range(j+1,l1):
                    sum=self.list[i]+self.list[j]+self.list[k]
                    if(sum==0):
                        sum_list.append([self.list[i],self.list[j],self.list[k]])               
        return sum_list
list=[int(item) for item in input("Enter the numbers : ").split(",")]
a=sum(list)
print("The numbers which makes the sum equal to 0 are : ",a.py_1())


##################################################################################################


print(" Question 9 ")

class check():
    def __init__(self,str):
        self.str=str

    def myfunc(self):
            count=0
            for i in range(0,len(self.str)):
                if(i%2!=0):
                    if(self.str[i-1]=="(" and self.str[i]==")"):
                        pass
                    elif(self.str[i-1]=="[" and self.str[i]=="]"):
                        pass
                    elif(self.str[i-1]=="{" and self.str[i]=="}"):
                        pass
                    else:
                        count+=1

            if(count==0):
                return "valid."
            else:
                return "invalid."
str=input("Enter the set of parenthesis to check whether it is valid or not : ")
a=check(str)
print("The set of parenthesis is ",a.myfunc())