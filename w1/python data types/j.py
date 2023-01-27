x = "basketball"

def myfunc():
  x = "chess"
  print("My favourite game is " + x)

myfunc()

print("My favourite game is " + x) 

def myfunc():
  global y
  y = "fascinating "

myfunc()

print("c++ is " + y)



z = "creative "

def myfunc():
  global z
  z = "fantastic"

myfunc()

print("yOU ARE  " + z)

x = ["apple", "banana", "cherry"]
print(type(x))   #list

x = ("apple", "banana", "cherry")
print(type(x))   #tuple

x = {"name" : "John", "age" : 36}
print(type(x))   #dict
print(len(x)) 
