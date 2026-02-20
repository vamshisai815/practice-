#PART1 = TASK OF THE PROJECT
# project Goal 

#create a program that:
#1 Customer name 
#2 Product name 
#3 Product price 
#4 Quantity 
#5 Calculate total bill 
#6 Applies discount
#if total>= 5000 print(10% discount)
#if total>= 2000 print(5% discount)
# otherwise print(no discount)
#7 Prints final bill summary 

customer_name = "Lav Acharya"
Product_name = "Boat Nirvana Airpods"
Price= 2500
quantity = 2 
total_bill = Price*quantity
# discount 
if total_bill>= 5000:
    discount = total_bill*0.10
elif total_bill>= 2000:
    discount = total_bill*0.05
else:
    discount= 0
final_amount = total_bill - discount     

print("\n------ BILL SUMMARY ------")
print("Customer Name:",customer_name)
print("Product Name:", Product_name)
print("Price",Price)
print("Quantity", quantity)
print("Total Amount:", total_bill)
print("Discount",discount)
print("Final Amount to Pay",final_amount)
print("--------------------😊😉😊THANK YOU VISIT AGAIN😊😊😊------------------------")

