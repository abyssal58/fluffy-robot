
print("QUESTION 1.)")

word=input('Enter a string: ')
length=len(word)
rev_str=''
for i in range(0,length):
   rev_str+=word[length-1-i]
print(rev_str)

####################################################################################################


print("QUESTION 2.)")

range_start=int(input('Enter start range'))
range_end=int(input('Énter end range' ))
num=int(input('Enter a number'))

for i in range(range_start,range_end+1):
    if i%num==0:        #Checking remainder for divisibility
        print(i,'is divisible by ',num)

####################################################################################################

print("QUESTION 3.)")

import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
if a+b>c and b+c>a and c+b>a:       #Checking if triangle is possible or not
  s=(a+b+c)/2                       #s is semi-perimeter
  area=round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
  print(f"The area of triangle is {area}")
else:
  print("Invalid input of sides,triangle not possible")

####################################################################################################

print("QUESTION 4.)")

n=int(input("Enter no of rows"))
for i in range(1,n):
    if i<6:
        k = i
    else:
        k = 10-i
    for j in range(1,n//2+1):
        if j<=k:
            print("*",end="")
    print()

####################################################################################################

print("QUESTION 5.)")

row=int(input(enter row))
k=0
for i in range(1,row):
    
    for j in range(1,i+1):
        if j<=i:
            if k<26:
                print(chr(65+k),end="")
            else:
                k=0
                print(chr(65+k),end="")
           
            k+=1
    print()
####################################################################################################

print("QUESTION 6.)")

lower_value = int(input("Enter the Lower Range Value : "))  
upper_value = int(input("Enter the Upper Range Value : "))    # input from user the lower and the upper range
  
print ("The Prime Numbers in this range are : ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):                           # Check for each number if it has any factor between 1 and itself
            if (number % i) == 0:                             # if YES, the code will move on
                break       
        else:  
            print (number)                                    # if NO, the code prints the number

####################################################################################################

print("QUESTION 7.)")

for i in range(1,501):
  if i%7==0 and i%11==0:
    print(i)

####################################################################################################

print("QUESTION 8.)")
pos=[]
neg=[]
odd=[]
even=[]
times={}
li=[]
for i in range(10):
    num=int(input("Enter the number "))
    li.append(num)
    if num>=0:
        pos.append(num)
    elif num<0 :
        neg.append(num)
    if num%2==0 :
        even.append(num)
    else :
        odd.append(num)
    if num not in times :
            times[num]=1
    else:
        times[num]+=1
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
print("Number of times each number occurs in the List",times)

####################################################################################################

print("QUESTION 9.)")

word_list=[]
elements=int(input('Enter total elements in the list'))
for word in range(1,elements+1):
  x=input('Enter a word ')
  word_list.append(x)

for element in word_list:
  occ=0                                 #counter for occurrences in a list
  for element1 in word_list:
    if element==element1:
      occ+=1
  print (f"{element} occurs {occ} times")
  
