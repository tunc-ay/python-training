# q1 > multiple

x = int(input("Please enter a number: "))
for i in range(1, 10):
    print(i*x)

for i in range(1,4):
    print("*****")
    for k in range(1,4):
        print("{} * {} = {}".format(i, k, i*k))


# q2 > prime number

y = int(input("Please enter a number: "))
primeNumber = True
if y == 1:
    primeNumber = False

for i in range(2, y):
    if y % i == 0:
        primeNumber = False
        break
if primeNumber:
    print("It is a prime number")
else: print("It is NOT a prime number")