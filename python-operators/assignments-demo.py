a, b, c = 2, 5, 10

# Q1 > input two numbers from user and multiply them. And find out the difference.

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(a + b + c)
calc = (x * y)-z
print(calc)

# Q2 > calculate // of c with b

q2 = float(c//b)
print(q2)

# Q3 > mod 3 of a + b + c

q3 = (a + b + c) % 3
print(q3)

# Q4 > calculate b ** a

q4 = b **a 
print(q4)

numbers = (1, 5, 7, 10, 3)

# Q5 > find c ** 3 after a, *b, c
a, *b, c = numbers
result = c ** 3
result1 = b[0] + b[1] + b[2]

print(a, b, c)
print(result)
print(result1)