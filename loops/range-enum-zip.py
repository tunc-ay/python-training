# Range

r = range(1, 3, 1)
result = list(r)
print(result)


for i in range(2):                      # no need to use the list.
    print(i)

for i in range(15, 95):
    if (i%2==0):
        print(i)

#Enumerate
brands = ["Apple", "Samsung", "Nike"]

obj1 = enumerate(brands)
print(list(obj1))

for i in enumerate(brands):
    print(i)

for index, value in enumerate(brands):
    print(index, value)

# zip method 
numbers1 = [1, 2, 3, 4, 5]
numbers2 = ["a", "b", "c", "d", "e"]

print(list(zip(numbers1, numbers2)))