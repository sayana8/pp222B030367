#loops
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#second variant 
  thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

  #while 
  thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

  #join tuples 
  fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)