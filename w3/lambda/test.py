#31.01.23
st= "abx"
print(len(st))

a =""" ab ababbbab
abababa ababab"""
print (len(a))

x=10
print (st + str(x) )  #abx10

val = "abcdefg"
#[0; len -1]
for x in range(len(val)):
    print(x)  #0-6


i = "asdfghjk"
for x in i:    #a s d f g h j k
    print(x)
  
valli="abcABC"
print(valli.isalpha()) #true
print(valli.isupper())  #false
print(valli.islower())  #false
wal="123456"
print(wal.isdigit())  #true 
we=" "
print(we.isspace() ) #true 

wer="pytHon123"
print(wer.upper())
print(wer.lower())
wes="py"
be="123"

print(wer.startswith(wes))  #true -> substr
print (wer.startswith(be))  #false 

print(wer.endswith(be))  #true 

print(wes.find("123"))  #-1
print(wer.find("123"))  #6

print(wer.find("python", 2))  #-1
print(wer.rfind("123"))    #6


wq="\n        kdcjdcdjcnsdjvcnb     \n "
print(wq.strip())

vals="asdfghjk  "
print(val.replace("a", "AAAAAAAA"))






