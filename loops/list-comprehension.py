numbers = [i for i in range(1,20)]

numbers1 = [i*i for i in range(1,20)]

numbers2 = [i+i for i in numbers]

print(numbers)
print(numbers1)
print(numbers2)

name = "Obiwan"
result= [i.upper() for i in name]
print(result)