lst = [1, 2, 3, 4, 5]
print("Original list:", lst)

# Add
lst.append(6)
print("After append(6):", lst)
lst.insert(2, 99)
print("After insert(2,99):", lst)
lst.extend([7,8])
print("After extend([7,8]):", lst)

# Remove
lst.pop()
print("After pop():", lst)
lst.pop(1)
print("After pop(1):", lst)
lst.remove(99)
print("After remove(99):", lst)

# Search & count
print("Index of 4:", lst.index(4))
print("Count of 2:", lst.count(2))

# Sort & reverse
lst.sort()
print("After sort():", lst)
lst.reverse()
print("After reverse():", lst)

# Copy & length
lst2 = lst.copy()
print("Copied list:", lst2)
print("Length of list:", len(lst))
