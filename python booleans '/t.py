print(10 > 9)    #true 
print(10 == 9)   #false 
print(10 < 9)    #false 

#example 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#evaluate a string and a number 
print(bool("Hello"))
print(bool(15))

#evaluate 2 variables 
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


bool("abc")   #true
bool(123)   #true
bool(["apple", "cherry", "banana"]) #true 


#false 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#CLASS and boolean variables 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))     #false


def myFunction() :
  return True

print(myFunction())  #true


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #yes

#check
  x = 200
print(isinstance(x, int))     #true 


