# q1 driver license conditions

driverName = input("Please enter your name: ")
driverAge = int(input("Please enter your age: "))
driverEdu = input("Please enter your education: ")

if driverAge >= 18: 
    if  driverEdu == "high school" or driverEdu == "university":
        print("You can have a driver license!")
    else: ("You cannot have a driver license!") 
else: print("You cannot have a driver license!") 

#q2 grade calculation

exam1 = float(input("Your first exam: "))
exam2 = float(input("Your second exam: "))
exam3 = float(input("Your third exam: "))
examTotal = float(exam1 + exam2 + exam3) / 3

if examTotal >= 85: 
    print("Your grade is 5")
elif examTotal <= 84 and examTotal >= 70: 
    print("Your grade is 4") 
elif examTotal <= 69 and examTotal >= 55: 
    print("Your grade is 3") 
elif examTotal <= 54 and examTotal >= 45: 
    print("Your grade is 2") 
elif examTotal <= 44 and examTotal >= 22: 
    print("Your grade is 1")
else: print("Your grade is 0")  

#q3 car inspection
import datetime

carDate = input("The time for your car(YY/MM/DD): ")
carDate = carDate.split('/')

now = datetime.datetime.now()
dif = datetime.datetime(int(carDate[0]), int(carDate[1]),int(carDate[2]))

difCalc = now - dif
difCalculation = difCalc.days
print(difCalculation)

if difCalculation <= 365: 
    print("See the first inspection")
elif (difCalculation > 365) and (difCalculation <= 365*2): 
    print("See the second inspection")
elif (difCalculation >= 365*2) and (difCalculation <= 365*3): 
    print("See the third inspection")
else: input("go home")
