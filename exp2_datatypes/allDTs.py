print("Welcome to Data Type Playground!\n")

# Choose data type
dtype = input("Choose data type (list/tuple/set/dict): ").lower()

if dtype == "list":
    lst = input("Enter list elements separated by commas: ").split(",")
    lst = [x.strip() for x in lst]  # remove spaces
    print("\nOriginal List:", lst)
    
    # Add elements
    lst.append("new_item")
    print("After append('new_item'):", lst)
    lst.insert(0, "first")
    print("After insert(0,'first'):", lst)
    lst.extend(["x","y"])
    print("After extend(['x','y']):", lst)
    
    # Remove
    lst.pop()
    print("After pop():", lst)
    if "x" in lst: lst.remove("x")
    print("After remove('x'):", lst)
    
    # Info
    print("Count of 'y':", lst.count("y") if "y" in lst else 0)
    if "first" in lst: print("Index of 'first':", lst.index("first"))
    print("Length:", len(lst))
    
elif dtype == "tuple":
    tup = input("Enter tuple elements separated by commas: ").split(",")
    tup = tuple(x.strip() for x in tup)
    print("\nOriginal Tuple:", tup)
    print("Count of first element:", tup.count(tup[0]) if len(tup)>0 else 0)
    print("Index of first element:", tup.index(tup[0]) if len(tup)>0 else None)
    print("First element:", tup[0] if len(tup)>0 else None)
    print("Last element:", tup[-1] if len(tup)>0 else None)
    print("Slice (1-3):", tup[1:4])
    print("Length:", len(tup))
    
elif dtype == "set":
    s = input("Enter set elements separated by commas: ").split(",")
    s = {x.strip() for x in s}
    print("\nOriginal Set:", s)
    
    # Add
    s.add("new_item")
    print("After add('new_item'):", s)
    s.update(["x","y"])
    print("After update(['x','y']):", s)
    
    # Remove
    s.discard("x")
    print("After discard('x'):", s)
    popped = s.pop()
    print("After pop() (random element removed):", s, "| Popped:", popped)
    
    # Info
    print("Is 'y' in set?", "y" in s)
    print("Length:", len(s))
    
elif dtype == "dict":
    print("Enter key:value pairs separated by commas (e.g., name:Jiten,age:20):")
    items = input().split(",")
    d = {}
    for item in items:
        if ":" in item:
            k,v = item.split(":")
            d[k.strip()] = v.strip()
    print("\nOriginal Dictionary:", d)
    
    # Access
    print("Keys:", d.keys())
    print("Values:", d.values())
    print("Items:", d.items())
    
    # Add / update
    d["new_key"] = "new_value"
    print("After adding new_key:", d)
    d.update({"age":"21"})
    print("After update({'age':'21'}):", d)
    
    # Remove
    d.pop("age", None)
    print("After pop('age'):", d)
    d.popitem()
    print("After popitem():", d)
    print("Length:", len(d))
    
else:
    print("Invalid data type! Choose list, tuple, set, or dict.")
