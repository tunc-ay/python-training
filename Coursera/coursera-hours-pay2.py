# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number.

hours = input("Enter hours: ")
rate = input("Enter rate: ")
extraHours = input("Any overwork hours: ")
try: 
    hoursFloat = float(hours)
    rateFloat = float(rate)
    extraHoursFloat = float(extraHours)
except:
    print("Please enter a numeric value")
    quit()

if extraHoursFloat >= 1:
    payment = ((rateFloat*1.5)*extraHoursFloat) + (hoursFloat*rateFloat)
else: 
    payment = hoursFloat * rateFloat
print("Your payment is", payment)