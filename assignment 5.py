
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
for i in range(1,6):
  c=0                       #c is a counter for printing '*'
  for j in range(1,i+1):
    c+=1
  print('*'*c)



a=4
while a>0:
  d=0                      #d is a counter for printing '*'
  for b in range(1,a+1):
    d+=1
  print('*'*d)
  a-=1
print( )

####################################################################################################

print("QUESTION 5.)")

alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rows=int(input("Enter number of rows"))
c=0
for i in range(1,rows+1):
  for j in range(1,i+1):
      print(alphabets[c%26],end="")           #use of end keyword for line formatting
      c+=1
  print()

####################################################################################################

print("QUESTION 6.)")

range_start=int(input("Enter starting range"))
range_end=int(input("Enter ending range"))
for num in range(range_start,range_end+1):
  c=0
  for i in range(1,num+1):
    if (num%i==0):
      c+=1
  if c==2:                              #prime number is divisible by only 1 and itself
    print(f"{num} is a prime number")

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
  
