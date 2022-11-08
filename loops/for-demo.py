numbers = [1, 5, 15, 35, 57, 72]
# q1 > write a loop to write every list item

for i in numbers:
    print(i)

# q2 > Which numbers in the set are a multiple of 5?
for i in numbers:
    if (i%5==0):
        print(i)

# q3 > find out the total

total = 0
for i in numbers:
    total = total + i
print(total)

# q4 > find the square of the even numbers

for num in numbers:
    if num % 2 == 0:
        print(num * num)

products = ['iPhone 8', 'iPhoneX', 'iPhoneXR', 'Samsung S10']

# q5 write the second character of every member in the list

for prod in products:
    print(prod[1])

# q6 list members with iPhone

for i in products:
    if 'iPhone' in i:
        print(i)