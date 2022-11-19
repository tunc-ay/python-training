# q1 > repeat the word provided by the user

x = input("Enter a word: ")
def greetings():
    print(x)
greetings()

for i in range(1):
    greetings()

# q2 > calculate the area and perimeter of a rectangle

def rectArea():
    a = float(input("Enter a rectangle's edge: "))
    b = float(input("Enter a rectangle's second edge: "))
    print(f"The area is " + str(a*b))
    print(f"The perimeter is " + str(2*(a+b)))
rectArea()

# q3 > heads or tails
import random
def cointoss():
    return random.choice(["Heads", "Tails"])
print(cointoss())

# q4 > identify all prime numbers between two numbers provided
def findPrime(num1, num2):
    for number in range(num1, num2+1):
        if number > 1:
            for i in range(2, number):
                if (number%i == 0):
                    break
            else: print(number)
findPrime(40, 70)

# q5 > divisor

def findDivisor(number):
    divisor = []
    for i in range(2, number+1):
        if (number % i == 0):
            divisor.append(i)
    return divisor
print(findDivisor(54))