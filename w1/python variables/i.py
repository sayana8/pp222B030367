x, y, z = "qwerty", "asdfgh", "zxcvbn"
print (x,y,z)

names =["Aruzhan", "Aqnur", "Amina"]
a, b, c = names 
print(a,b,c) 
q="My "
w="name "
e = "is "
print (q + w + e )

print (q,w,e) 
my_vari_able = "156"
MyVariableIs = "string"
a = " "
print (my_vari_able + a +MyVariableIs) 




#function 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()   #Python is awesome 

#function2

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#output -> python is fantastic \n python is awesome 

#global 

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#global2
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)