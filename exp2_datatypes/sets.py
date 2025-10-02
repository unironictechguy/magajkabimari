s = {1, 2, 3}
print("Original set:", s)

# Add
s.add(4)
print("After add(4):", s)
s.update([5, 6])
print("After update([5,6]):", s)

# Remove
s.remove(2)
print("After remove(2):", s)
s.discard(10)  # no error even if 10 not present
print("After discard(10):", s)
popped = s.pop()  # removes a random element
print("After pop():", s, "| Popped element:", popped)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Symmetric difference:", a ^ b)

# Membership & length
print("Is 3 in s?", 3 in s)
print("Length of s:", len(s))
