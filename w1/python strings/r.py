age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

price = 1455
txt = "The price of the notebook is {} dollars"
print(txt.format(price))

price = 49.2555
txt = "The price is {:.3f} dollars"
print(txt.format(price))

a = 3
b= 567
c = 49.455
math = "I want to sum {} apples ,{} oranges and {:.2f} dollars."
print(math.format(a, b, c))
#second variant of this 

a = 3
b= 567
c = 49.455
math = "I want to sum {0} apples ,{1} oranges and {2:.2f} dollars."
print(math.format(a, b, c))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Mercedes", model = "G63"))

a = 450
b = 144
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  if a > b: print("a is greater than b")

a = 33
b = 200

if b > a:
  pass #continue