#q1 > check whether the number provided is between 50 and 100.
x = int(input("Enter a number: "))
if (x > 50 and x < 100):
    print("Your number is between 50 and 100")
else: print("Your number is not within the range.")

#q2 > check whether the number provided is positive and odd.

y = int(input("Enter a number: "))
if y > 0:
    print("Your number is positive")
else: print("Your number is not positive")
if y % 2 == 1:
    print("Your number is odd")
else: print("Your number is not odd.")

#q3 > check username and password
x = input("Enter your username: ")
y = input("Enter your password: ")
if (x == "info@obiwankenobi.com" and y == "123456"):
    print("Your information is correct")
else: print("Ooppss...")

#q4 > two midterms (0.6) and one final (0.4).
# if bigger than 50, pass. 
# conditions > final must be at least 50
# if the final is 70, pass directly.

midterm1 = int(input("Enter first midterm point: "))  
midterm2 = int(input("Enter second midterm point: "))  
final = int(input("Enter final point: "))  
passPoint = (((midterm1 + midterm2)/2)* 0.6) + (final * 0.4)
if final < 50:
    print("The final point is less than 50, so you failed")
if final > 70: 
    print("The final point is bigger than 70, so you passed")
elif passPoint >= 50:
    print("Your average is " + str(passPoint) + ", You passed!")

#q5 > get name, height, and weight. calculate the obesity.

name = input("Please enter your name: ")
height = int(input("Please enter your height: "))
weight = int(input("Please enter your weight: "))
calculateObesity = weight / (height*height)
if calculateObesity < 18.4: print("Your are slim!")
elif calculateObesity >= 18.5 and calculateObesity <= 24.9: print("Your are normal!")
elif calculateObesity >= 25.0 and calculateObesity <= 29.9: print("You are overweight!")
elif calculateObesity >= 30.0 and calculateObesity <= 34.9: print("You are obese!")
else: print("You are out of range!")