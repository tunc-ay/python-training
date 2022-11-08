numbers = [4, 6, 9, 10, 35, 57, 89, 125, 244]

# q1 > write all numbers with the while loop

# index = 0
# while index < len(numbers):
#     element = numbers[index]
#     print(element)
#     index += 1

# q2 > input two numbers, and list the odd numbers betwen these two user-entered numbers.

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# i = x
# while i < y:
#     if (i%2==1):
#         print(i)
#     i += 1

# q3 > count from 100 to 1

# i = 100

# while i > 0:
#     print(i)
#     i -= 1

# q4 > get 5 numbers and list them in order

numbers = []
i = 0
while i < 5:
    num = int(input("Enter the first number: "))
    numbers.append(num)
    i += 1
numbers.sort()
print(numbers)