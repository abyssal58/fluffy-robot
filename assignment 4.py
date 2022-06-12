print("QUESTION 1.)")

Marks=int(input("Enter Marks: "))
if(Marks<100 and Marks>=0):
    if(Marks<25):
        print("Grade = F")
    elif(Marks>=25 and Marks<45):
        print("Grade = E")
    elif(Marks>=45 and Marks<50):
        print("Grade = D")
    elif(Marks>=50 and Marks<60):
        print("Grade = C")
    elif(Marks>=60 and Marks<80):
        print("Grade = B")
    elif(Marks>=80):
        print("Grade = A")
else:
    print("Invalid Input of Marks")
    
####################################################################################

print("QUESTION 2.)")

Year=int(input("Enter Year = "))
if(Year%4==0):
    if(Year%100==0):
        if(Year%400==0):
            print("Year is a leap year.")
        else:
            print("Year is not a leap year")
    else:
        print("Year is a leap year")
else:
    print("Year is not a leap year")
    
#####################################################################################

print("QUESTION 3.)")

import random

for i in range(1,11):
  a = random.randint(1,10)
  b = random.randint(1,10)
  ans = int(input(f'Question{i}:{a}x{b}='))
  if ans==a*b:
    print("Correct")
  else:
    print(" Incorrect, try again ")
    
######################################################################################
    
print("QUESTION 4.)")

for no_of_candy in range(200):
    if(no_of_candy%5==2 and no_of_candy%6==3 and no_of_candy%7==2):
        print("Possible No of Candies: ",no_of_candy,"\n")
    
    
    