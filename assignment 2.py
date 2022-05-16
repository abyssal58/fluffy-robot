print("QUESTION 1.)")
input_string="Python is a case sensitive language"
#a.) FIND THE LENGTH OF THE INPUT STRING.
print("PART A")
print(len(input_string))

#b.) REVERSE THE ORDER OF THE STRING IN ONE LINE CODE.  
print("PART B")
print(input_string[::-1])

#c.) USING SLICING FUNCTION STORE "A CASE SENSITIVE" IN NEW STRING.
print("PART C")
sliced_string=input_string[10:26]
print(f"SLICED STRING IS:  {sliced_string}")

#d.) REPLACE "A CASE SENSITIVE" WITH "OBJECT ORIENTED".
print("PART D")
print(input_string.replace("a case sensitive","object oriented"))

#e.) FIND INDEX OF SUBSTRING "A" IN THE GIVEN INPUT STRING.
print("PART E")
print(input_string.find("a"))

#f.) REMOVE THE WHITE SPACES FROM THE GIVEN INPUT STRING.
print("PART F")
print(input_string.replace(" ",""))


##################################################################################################

print("QUESTION 2.)")
# STORE YOUR NAME,SID,DEPARTMENT,CGPA INTO DIFFERENT VARIABLE.THEN PRINT WITH THE HELP OF STRING FORMATTING
name="Arnav Sharma"
SID=21102085
department="CIVIL"
CGPA=9.9
print(f"Hey,{name} Here!\nMy SID is {SID}\nI am from {department} department and my CGPA is {CGPA}")

####################################################################################################


print("QUESTION 3.)")
# FOR A=56 AND B=10 WITH THE HELP OF BITWISE OPERATOR CALCULATE THE FOLLOWING:
a=56
b=10
print("a&b is: ",a&b)
print("a|b is: ",a|b)
print("a^b is: ",a^b)
print("a<<2:",a<<2,"\tb<<2: ",b<<2)
print("a>>2:",a>>2 ,"\tb>>4: ",b>>4)


###########################################################################################################

print("QUESTION 4.)")
# WRITE A PYTHON PROGRAM TO CHECK IF THE WORD "NAME" IS PRESENT IN THE STRING ENTERED BY THE USER.
string=input("ENTER ANY STRING : ")
s=string.find("name")
if s==-1:
    print("NO")
else:
    print("YES")   

#############################################################################################################

print("QUESTION 5.)")
a = int(input("ENTER LENGTH OF FIRST SIDE OF TRAINGLE: "))
b = int(input("ENTER LENGTH OF SECOND SIDE OF TRAINGLE: "))
c = int(input("ENTER LENGTH OF THIRD SIDE OF TRAINGLE: "))
d = a + b <= c or a + c <= b or c + b <= a
match d:
    case True:
        print("YES")
    case False:
        print("NO")
    
#############################################################################################################

print("QUESTION 6.)")
a = int(input("enter a number : "))
b = int(input("enter another number : "))

count = 0
while (a>0 or b>0):
    t1 = a&1
    t2 = b&1
    if t1!=t2:
        count+=1
    a = a>>1
    b = b>>1
    
print(count)

#############################################################################################################
