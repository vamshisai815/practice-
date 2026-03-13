#Practice Questions

#?1 Create two sets and find the union of sets
setA= {23,90,39}
setB = {45,17,59}
result = setA.union(setB)
print(result)

#?2 Create two set and find the intersection of sets 
numbers1 = set(input("Enter numbers: ").split())
numbers2 = set(input("Enter Your number2: ").split())
result=  numbers1.intersection(numbers2)
print(result)


#?3 Create two sets and find difference of sets 

food1 = set(input("Enter Your food1").split())
food2 = set(input("Enter Your food2").split())
final_output = food1.difference(food2)
print(final_output)

#?4 Create a set of 5 numbers and print it 

set1 = {89,67,90,35,12}
print(set1)

#?5 Create a set of 3 fruits and add a new fruit "Mango"

Fruits = {"Pinapple", "orange","Strewberry"}
print(Fruits)
Fruits.add("Mango")
print(Fruits)

#?6 Create a set of 4 colors and remove "Red"from the set 

Colors = {"Green","Red","Blue","Black"}
print(Colors)
Colors.remove("Red")
print(Colors)

#?7 Create a set of 6 numbers and print the total number of elements

numbers= set(input("Enter Your numbers").split())
print(numbers)
print("The Total Numbers is: ",len(numbers))

#?8 create a set of cities and check whether "Mumubai" exists in the set

cities = set(input("Enter Your Faviorite Cities Name:").split())
print(cities)
if "Mumbai" or "mumbai" in cities:
    print("Mumbai is in cities")
else:
    print("Mumbai is not in Cities")

#?9 Two Student like difference sports 
#!Student1 = {"Cricket","Football","Tennis"}
#!Student 2 = {"Football","Hockey","Cricket"}
#? Find Common Sports

student1 = {"Cricket","Football","Tennis"}
student2 = {"Football","Hockey","Cricket"}
Result = student1.intersection(student2)
print("The common Sports is :",Result)

