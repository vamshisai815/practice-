# # SETS in Python 

# creating a sets 
info = {"Carla",18,False,5.9}
print(info)

# #! Accessing set items :
# Using A For loops

info = {"Carla",19,False,5.9}
for i in info:
    print(i)

# #! joinng sets 
# #* union() 

cities= {"Bilaspur","Raipur", "Korba","Delhi","Jaipur"}
cities2 = {"Jodhpur","udaipur", "bhopal","Indore"}
cities3 = cities.union(cities2)
print(cities3)

# #* update()
set1 = {1,2,3}
set2 = {3,4,5}
set1.update(set2)
print(set1)

#* intersection()
set1 = {1,2,3,4,5}
set2 = {2,3,8,9,10}
result= set1.intersection(set2)
print(result)

#*intersection_update()
set1 = {12,34,55,66,89}
set2 = {34,22,90,12,43}
set1.intersection_update(set2)
print(set1)

#*symmetic_difference 
cities= {"Kanpur","Jaipur","ujjain","Bhopal"}
cities2 = {"Indore", "Jaipur", "vizag","Bhopal"}
result= cities.symmetric_difference(cities2)
print(result)

#*symmetrc_diffference_update

cities= {"Kanpur","Jaipur","ujjain","Bhopal"}
cities2 = {"Indore", "Jaipur", "vizag","Bhopal"}
cities.symmetric_difference_update(cities2)
print(cities)

#* difference() 
numbers1 = {1,2,3,4}
numbers2 = {2,4,8,9}
Difference = numbers2.difference(numbers1)
print(Difference)

#* Difference_update 

number1 = set(input("Enter Your Number:").split())
nummber2 = set(input('Enter Your Number:').split())
number1.difference_update(nummber2)
print(number1)

