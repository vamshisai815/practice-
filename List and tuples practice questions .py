#?Ask The user For their 3 Favorite movies and Store Them in a list 

Movie1 = input("Enter Your Movie1:")
Movie2 = input("Enterr Your Movie2:")
Movie3 = input("Enter Your Movie3:")
Movie4 = input("Enter Your Movvie4:")
Movie5 = input("Enter Your Movie5:")

Movielist=[]

Movielist.append(Movie1)
Movielist.append(Movie2)
Movielist.append(Movie3)
Movielist.append(Movie4)
Movielist.append(Movie5)

print(Movielist)
print(len(Movielist))

#? Create a Tuple of Marks ( 87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min()

Marks = (87,64,33,95,76)
print(max(Marks))
print(min(Marks))
print(Marks.count(33))
print(Marks.index(95))

#? Student Makrks LIst(Basic list)
# ?Create a list of 5 subjects marks of a bcom student 
# *Tasks : 
#*1Print the list 
#*2 Print the highest mark 
#*3 Print the lowest mark 
#*4 Print total marks 
#*5 Print average marks 
 
Marks = [87,90,77,98,45]
print(Marks)
print("The Highest marks:", max(Marks))
print("The Lowest Marks:",min(Marks))
print("The Lowest Marks:",sum(Marks))
print("The Average Marks:",sum(Marks)/len(Marks))

#? Monthly Expenses(List operations)
#? Create a list of monthly expenses:
#! Rent = 5000
#! Food = 3000
#! Travel = 1500
#! Internet = 800
#TODO = 1  Add an New Expense (Books = 1200)
#ToDO = 2 Remove internet expense 
#TODO = 3 Print Updated list 
#TODO = 4 Print Total Expenses 

expense = [5000,3000,1500,800]
expense.append(1200)
expense.remove(800)

print("Update list",expense)
print("Total Expenses=",sum(expense))

#?3 Product Prices (Tuple)
#? Create a Tuple of 4 product prices in a small shop
#? (100,250,400,150)
#TODO= 1 Print The Tuple 
#TODO= 2 Print FIrst Price 
#TODO =3 Print Last Price
#TODO = 4 Print total Price 

Product_Price = (500,450,900,133)
First_Price = Product_Price[0]
Last_Price = Product_Price[3]
Total_Price = sum(Product_Price)

print("The Product Price =", Product_Price)
print("The First Price = ",First_Price)
print("The last Price = ",Last_Price)
print("The Total Price=",Total_Price)

#? Bank Traction Record 
#! Create a tuple of Transaction IDS : ("TXN101","TXN102",TXN103)
#! Createa list of transaction amounts: [2000,3500,1500]
#TODO1 Print Transaction IDS
#TODO2 Print Transaction Amounts 
#TODO3 Print Total Transaction Amount 
#TODO4 Add New Amount 4000 to the list 

Transaction_IDS = ("TXT101","TXN102","TXN103")
Transaction_Amounts = [2000,3500,1500]
print("Transaction IDS = ",Transaction_IDS)
print("Transaction Amount =",Transaction_Amounts)
print("Total Transaction_Amounts =", sum(Transaction_Amounts))
Transaction_Amounts.append(4000)
print(Transaction_Amounts)

#? Daily Sales List 
#? Create A List of 7 days sales of a shop 
#TODO1 Print sales
#TODO2 Print Highest Sale
#TODO 3 Print Lowest Sale
#TODO 4 Print Total weekly sale

Sales = [7000,9000,5000,6400,3000,2400,1900]
print("The sales = ",Sales)
print("The Highest Sale = ",max(Sales))
print("The Lowest Sale = ", min(Sales))
print("The Total Sales = ",sum(Sales))
#?Product Stock List
#?Create a list of product stock: [50, 30, 20, 100]
#TODO :
#!Add new stock 60
#!Remove stock 20
#!Print total stock

Stock = [50,30,20,100]
Stock.append(60)
Stock.remove(20)
print("The Total Stock",sum(Stock))
print("The Update list",Stock)

