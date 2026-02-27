# LIST in python 
food = ["Chole Bathure", "Choco waffle", "gulab jamun", "apple", "mango"]
print(len(food))
print("first value of the food list is ",food[0])
print("Third vlaue of the food list is", food[3])

# Modifying the list 
food[0] = "Samosa"
print(food)
# list Slicing 
Marks = (87,64,33,95,76)
print(Marks[1:4])
print(Marks[:3])
print(Marks[-3:-1])

#  List Function 
print(len(Marks))
print(max(Marks))
print(min(Marks))

# Method in list 

students_details = ["Vamshi Sai", "18", "Bilaspur", ]
students_details .append("chhatisgarh")
print(students_details)
students_details.insert(1,"19")
print(students_details)
students_details.remove("Bilaspur")
print(students_details)
students_details.count("a")
print(students_details)
students_details.sort()
print(students_details)
students_details .reverse()
print(students_details)

#Practice Question 
# write a program that takes names of 5 favorite places in india from the user and store them in a list. Then point the list and its length 

# favorite_place = input("Enter Your Favorite Places in india:")
# print(favorite_place)
# print(len(favorite_place))


# Tuples in Python 
tup = (87,64,33,95,76)
print(type(tup))
print(tup)

# Tuples Example 
t1 = () # empty tuple 
t2 = (1,) # single element tuple 
 
 # Immutable Tuple 
# tup = (10,20,30)
# tup[0] = 100 
# print(tup)  # Error 

#Practice question
#Create a tuple of Your favorite 5 fruits 
# Then Print :
#1) Total Numbers of fruits 
#2) The Index of one selected fruits 

fruits = ["Mango","Apple","Watermelon","Banana", "Strew barry"]
print(len(fruits))
print(fruits[3])

