# Calculations on circle
pi = 3.14
r = float(input("x: "))
circle = pi * (r**2)
circle2 = 2 * pi * r
print(circle, circle2)
result = "alan: " + str(circle) + " çevre:" + str(circle2) # we can mix them like this.
print(result)

##the following is converting km into mile
roadTrip = float(input("y: ")) #km info
mil = roadTrip / 1.609344
print(mil)

# the following is converting USD into Euro
moneyUSD = float(input("How much USD do you have: "))
moneyConversion = moneyUSD * 1.02
result1 = "Your USD in Euro is " + str(moneyConversion)
print(result1)
