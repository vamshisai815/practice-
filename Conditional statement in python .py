#Conditional Statement 


 #if statement  
 
marks = 70 
if(marks>=65):
    print("Your grade is A")


# elif statement 

marks= 85 

if(marks>=90):
    print("Your grade is A ")

elif(marks>=80):
    print("Your grade is B")

# else statement 

age = 18
if(age>=18):
    print("You are eligible for giving the vote")
else:
    print("You are not eligible for giving the vote")


# practice question
#write a python program takes a number as input and print
#"Postive" if the number >0
# "Zero" if the number == 0 
#"Neative" if the number <0

num = int(input("Enter your number"))

if(num>0):
    print("Postive")
elif(num==0):
    print("Zero")
else: 
    print("Negative")