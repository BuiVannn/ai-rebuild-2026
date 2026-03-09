data_type = ["numbers", "strings", "lists", "dictionaries", "tuples", "files", "sets", "other core types", "program unit types", "implementation-related types"]
print(data_type)

"""
Thư viện math
Thư viện random
number, string, tuples là immutable (bất biến)
list, dictionary, set là mutable (có thể thay đổi)
"""
import math
print(math.pi)

import random
print(random.random())
print(random.choice(["a", "b", "c", "d"]))

text = "Hello, World!"
print(len(text))
print(text[1:5])
print(text[0:-1])
print(text[1:])
print(text[:5])
print(text[-6:-1])
print(text[:])
print(text * 3)
# không chạy được text[0] = "h" vì chuỗi là bất biến (immutable)
text = "h" + text[1:]
print(text)
print(text.find("o"))
print(text.replace("o", "0"))