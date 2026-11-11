number = [1, 2, 3]
number.append(4)

print(number)

name = "python"
name = name + " programming"
print(name)

# ---------------------------------------------
# List vs Tuple vs Set vs Dictionary
# ---------------------------------------------

# List: ordered, mutable, allows duplicates
fruits = ["apple", "banana"]
fruits.append("cherry")
print("List:", fruits)

# Tuple: ordered, immutable, allows duplicates
point = (10, 20)
print("Tuple:", point)
# point[0] = 5  # TypeError: tuples can't be changed

# Set: unordered, mutable, unique items only
tags = {1, 2, 2, 3}
print("Set:", tags)
print("Intersection:", tags & {2, 3, 4})

# Dictionary: key -> value mapping, keys are unique
user = {"name": "Ana", "age": 30}
user["email"] = "ana@example.com"
print("Dictionary:", user)

# ---------------------------------------------
# == vs is
# ---------------------------------------------

# == compares values, is compares identity (same object in memory)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True  -> same contents
print(a is b)  # False -> two separate list objects
print(a is c)  # True  -> c is the same object as a

# Use `is` for singletons like None
x = None
print(x is None)  # True

# Gotcha: small ints are cached by CPython, don't rely on `is` for numbers/strings
m = 256
n = 256
print(m is n)  # True only because of caching

# ---------------------------------------------
# *args vs **kwargs
# ---------------------------------------------

# *args collects extra positional arguments into a tuple
def add_all(*args):
    print("args:", args)
    return sum(args)

print(add_all(1, 2, 3, 4))  # 10

# **kwargs collects extra keyword arguments into a dict
def show_info(**kwargs):
    print("kwargs:", kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_info(name="Ana", age=30)

# Using both together (order: normal, *args, **kwargs)
def combo(required, *args, **kwargs):
    print(required, args, kwargs)

combo("hello", 1, 2, x=10, y=20)

# Unpacking when calling: * for sequences, ** for dicts
nums = [1, 2, 3]
print(add_all(*nums))        # same as add_all(1, 2, 3)
info = {"name": "Bob", "age": 25}
show_info(**info)            # same as show_info(name="Bob", age=25)
