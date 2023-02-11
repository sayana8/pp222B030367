def my_function():
  print("Hello from a function")

my_function()
#################

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#################

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
###############

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") # The youngest child is Linus
#############

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #The youngest child is Linus
#############

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") # His last name is Refsnes
#############

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") #I am from Sweden
my_function("India") # I am from India
my_function() # I am from Norway
my_function("Brazil") # I am from Brazil
#############

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits) 
#############

def my_function(x):
  return 5 * x

print(my_function(3)) # 15
print(my_function(5)) # 25
print(my_function(9)) # 45
#############

def myfunction():
  pass
###########

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
# Recursion Example Results 1 3 6 10 15 21