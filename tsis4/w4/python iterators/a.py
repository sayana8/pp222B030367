mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

"""output:
apple
banana
cherry 
"""
#same output by looping 
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)