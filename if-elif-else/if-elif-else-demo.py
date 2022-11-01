# benzin mi dizel mi
# 100 kilometrede ne kadar yakıyor
# kaç kilometre gideceksiniz


carFuel = input("Enter your fuel type: ")
fuelConsumption = float(input("Enter your consumption per kilometer: "))
miles = float(input("How many kilometers will you go: "))
gasolinePrice = 10
dieselPrice = 15
if carFuel == "gasoline":
    print(fuelConsumption * miles * gasolinePrice) 
elif carFuel == "diesel":
    print(fuelConsumption * miles * dieselPrice)



