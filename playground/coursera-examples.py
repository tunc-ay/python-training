# this is a playground to learn functions.

def greet (lang):
     if lang == 'es':
         print("Hola")
     elif lang == 'tr':
         print("Merhaba")
     else:
         print("Hello")

# use of Return

def greet (lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'tr':
        return "Merhaba"
    else:
        return "Hello"
print(greet('tr'), "Tyler")

# use of more parameters
def multiplyTwo(a, b):
    multiply = a * b
    return multiply
x = multiplyTwo(3,5)
print(x)
