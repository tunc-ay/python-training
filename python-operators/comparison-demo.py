# q1 > input two numbers and find out which one is bigger

x = input("x: ")
y = input("y: ")
if x > y:
    print("x is bigger")
else:
    print("y is bigger")

# q2 > find out whether a number is odd or even
z = int(input("enter a number: "))
z = int(z%2)
if z == 0:
    print("your number is even")
else: print("your number is odd")


# q3 > find out whether a number is positive or negative
z = int(input("enter a number: "))
if z > 0:
    print("Your number is negative")
else: print("Your number is positive")

# q4 > calculate midterm (60%) and final exam(40%). 
# if the median is 50 or more, pass. Otherwise, fail.

x = float(input("Enter your midterm exam: "))
y = float(input("Enter your final exam: "))
result = (x*0.6) + (y*0.4)
if result >=50:
    print("You passed!")
else: print("You failed!")

# q5 > Request email and password information and find out whether they match with existing info.
# user: info@obiwankenobi.com, pass:123456

x = input("Enter your username: ")
y = input("Enter your password: ")
if (x == "info@obiwankenobi.com" and y == "123456"):
    print("Your information is correct")
else: print("Ooppss...")