mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

"""
b
a
n
a
n
a
"""


#sam eoutput by looping
mystr = "banana"

for x in mystr:
  print(x)