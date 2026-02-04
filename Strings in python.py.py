# Strings in python
#examples 
str1 = "Hello"
str2 = "Vamshi Sai"
str3 = "Welcome to python!"

print(str1)
print(str2)
print(str3)

#Strings concatenation
str1 = "Hello"
str2 = "sai"

print(str1 + str2)

#length of strings 

print(len("Gulab Jamun"))
print(len("TVamshiSai"))

#for space 
str1 = "Hello"
str2 = "sai"

print(str1 + "  " + str2)
print(len(str1))

#indexing 


str= "Samosa" 
print(len(str))
print(str[0])
print(str[3]) 

#practice question 
#write a python program takes a user name as input and print
#1 the first Character 
#2 the last character 
#3 the total length of the name 

str1 = "Vamshi"
length = len (str1)

print(str1[0])
print(str1[5])
print(length)


name = "vamshi"

# Printing first character
print("First character:", name[0])

# Printing last character
print("Last character:", name[-1])

#slicing 

#example 
str = "GulabJamun"
print(str[0:5])
print(str[ :6])
print(str[5: ])

#code 

str="Gulabjamun"
firsthalf = str[0:5]
trialfirsthalf = str[:5]

print(firsthalf)
print(trialfirsthalf)

secondhalf = str[5:10]
trialsecondhalf = str[5:]

print(secondhalf)
print(trialsecondhalf)

#Common strings in python 

str = "Vamshi"

print(str.upper())
print(str.lower())
print(str.title())
print(str.find("Va"))
print(str.count("s"))
print(str.replace("hi","shi"))

#practice Qyestion 

#write a python program 
#Takes a senence as a input 
#converts it to lower case 
#Replace all spaces " " with underscores "_"

str= input("Enter your name")
print(len(str))
print(str.lower())
print(str.replace(" ", "_"))
print(str.upper())
print(str.find("a"))
print(str.count("a"))
print(str.capitalize())
print(str.endswith("o"))

# Assignment set 3 

#1 write a program that takes a sentence and prints 
# Total characters (length)
# uppercase version
# lowercase Version 


str = input("Enter Your sentence")

print(len(str))
print(str.upper())
print(str.lower())

#2 write a python program that takez any words as input and print- 
#The first letter of the word
# The last letter of the word 

str1 = input("Enter your word")


