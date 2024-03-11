#Dictionaries store elements in key/value pairs, i.e, keys are unique identifiers that are associated with each value.
# collection which is ordered** and changeable. No duplicate members.
capital_city={"Kenya":"Nairobi", "Uganda":"Kampala", "Tanzania":"Dodoma", "Rwanda":"Kigali", "Burundi":"Bujumbura"}
#Here keys are Kenya, Uganda etc and values are Nairobi, Kigali etc
capital_city["South Sudan"]="Juba"
print(capital_city)
#Accessing elements in a dictionary using keys
print(capital_city["Kenya"])
#Using the update() method to add items to a dictionary
capital_city.update({"Ethiopia":"Addis Ababa"})


numbers = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
print(1 in numbers)