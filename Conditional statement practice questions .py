#1 Bank Minimum Balance Check 
# Take account balance as input 
# if balance <1000 Then print "Minimum  balance not mentioned"
# Else- print(Account is active)

Account_balance = float(input("Enter Your Account Balance:"))

if Account_balance < 1000 :
    print("Minimum Balance not mwaintained")
else:
    print("Account is Active")

#2) Simple Interest Eligibility 
# IF Loan amount > 500000 - interest rate = 10% 
#else - interest rate= 7% 

Loan = float(input("Enter Your loan Amount:"))
time = float(input("Enter the time of loan in years: "))
if Loan > 500000:
    rate = 0.10 
else:
    rate = 0.07
interest = Loan*time*rate 
print("The total Interst Amount is :", interest)

#3) Grade Calculator 
# Take marks (0-100)
# 90+ - Grade A 
#75-89- Grade B
# 50-74 - Grade C 
# Below 50 - Grade F

marks= float(input("Enter Your Good Marks:"))
if marks >= 90:
    print("Grade A ")
elif marks >= 75-89:
    print("Grade B")
elif marks >= 50-74 : 
    print("Grade C")
else :
    print("Grade F")

#4) Largest Of Two Numbers 
# Take two Numbers and print the largest one 
# if both eaual - Print("Both numbers are equal")

a= int(input("Enter Your First Number:"))
b = int(input("Enter Your Second Number:"))
if a > b:
    print("The Larger Number is A ")
elif b>a:
    print("The Largest Number is B ")
else :
    print("Both numbers are equal")

#5) Salary Bonus Calculation 
# If employee salary >= 50000- Bonus= 20% 
# If Salary >= 30000- Bonus = 10%
# else = Bonus = 5% 

Salary = int(input("Enter Your Salary Here"))
if Salary >= 50000:
    Bonus = Salary*0.20
elif Salary >= 30000:
    Bonus = Salary*0.10
else:
    Bonus = 0.05
print("Bonus Amount:",Bonus)

#6) Electricity Bill Calculation
# Unit Consumed:
#0-100 = rs 2 per unit 
#101-200 = rs 5 per unit 
#Above 200 = RS 8 per unit 

unit = int(input("Enter Your Electricity Unit:"))
if unit <= 100: 
    bill = unit *2
elif unit<=200:
    bill = unit *5
else:
    bill = unit*8
print("Total BIll", bill)

#7) Online Shopping Discount 
# Take a Input as 
# Total purchase Amount
# is the user a premium member 
 
Purchase_Amount = int(input("Enter Your Purchase Amount"))
Premium_member = input("is you are premium user")

if Purchase_Amount>=5000:
    discount = Purchase_Amount*0.20/100
elif Purchase_Amount >= 2000:
    discount = Purchase_Amount *0.10/100
else:
     discount=0 

Premium_member= discount*0.05/100

print("Purchase Amount",Purchase_Amount)
print("Premium Member",Premium_member)
print("Discount Allowed",discount)




