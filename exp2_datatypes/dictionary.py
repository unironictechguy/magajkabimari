my_dict = {"name": "anand", "age": 20, "city": "Gandhinagar"}
print("Original dictionary:", my_dict)

# Access
print("Name:", my_dict["name"])
print("Country (get):", my_dict.get("country"))

# Keys, values, items
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# Add & update
my_dict["country"] = "India"
print("After adding country:", my_dict)
my_dict.update({"age":21,"city":"Ahmedabad"})
print("After update:", my_dict)

# Remove
my_dict.pop("age")
print("After pop('age'):", my_dict)
my_dict.popitem()
print("After popitem():", my_dict)
my_dict.clear()
print("After clear():", my_dict)
