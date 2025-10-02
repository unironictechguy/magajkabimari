# Interactive String Playground
text = input("Enter any string: ")

print("\nOriginal String:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())
print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())
print("Is Alphabetic?", text.isalpha())
print("Is Alphanumeric?", text.isalnum())
print("Count of 'a':", text.count("a"))
print("Find 'a':", text.find("a"))
print("Starts with 'H'?", text.startswith("H"))
print("Ends with '!'?", text.endswith("!"))
words = text.split()
print("Split into words:", words)
joined = "-".join(words)
print("Join words with '-':", joined)

# Indexing & slicing
if len(text) > 0:
    print("First character:", text[0])
    print("Last character:", text[-1])
if len(text) > 5:
    print("Slice (1-6):", text[1:6])

# String formatting demo
name = input("\nEnter your name for formatting demo: ")
age = input("Enter your age: ")
formatted = "Hello {}! You are {} years old.".format(name, age)
f_string = f"Hello {name}! You are {age} years old."
print("Formatted string (.format):", formatted)
print("Formatted string (f-string):", f_string)
