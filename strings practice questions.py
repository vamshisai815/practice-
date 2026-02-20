#Q1)  create a strings variable Company_name and print it 


company_name = input("Please Enter your company name:")

print(company_name)

#2) Take a user's name as input and print Welcome <name> to our comapany 

name = input("Enter your name")

print("Welcome",name,"to our company") 

#3) Store a product name in a string and print the length of the string

str = "Boat Earpods"
print(len(str))

# #4) Take a sentence as input and print it in uppercase and lowercase 

str = input("Enter Your sentence")

print(str.upper())
print(str.lower())

# #5 Given a string "Business Accounting",Print only the word Accounting using string slicing

str = "Business Accounting"
slicing = str[9:19]
print(slicing)

#Q7) Take a user's email ID and print the domain name (Example gmail.com)

Email_id = input("Enter your Email ID :")
domain_name = Email_id[4:13]
print(domain_name)

#Q8) Replace the word "OlD" with "New" in the string "This is an old policy"

str = "This is an old policy"
print(str.replace("old","New"))

#Q9) Count how many times the letter "a" apppears in the string "management"

str = "Management"
print(str.count("a"))

#Q10) Take a users full name and print the first character of the name 

str = input("Enter your full name")
print(str[0])



