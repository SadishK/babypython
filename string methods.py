"""
Author: SadishDK
Practicing string methods
"""

# Accessing characters in a string
# index starts from zero
first = "nyc"[0]
city = "sfo"
print(first)
ft = city[0]
print(ft)


"""
len()
lower()
upper()
str()
"""

stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))

"""
Concatenation
"""
print("Hello " + " " + " World !!!")
print(first + " " + city)