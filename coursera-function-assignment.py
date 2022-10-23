hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
hoursExtra = float(hours-40)
rateExtra = hoursExtra * (rate * 1.5)
def computepay(a, b, c, d):
    if c < 0:
        c = 0
    paymentCalc = (a - d) * b + c
    return paymentCalc
x = computepay(hours, rate, rateExtra, hoursExtra)
print("Pay",x)