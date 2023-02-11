#4
n = [int(i) for i in input().split()] 
def is_prime(n):
    for num in n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
is_prime(n)

 
    