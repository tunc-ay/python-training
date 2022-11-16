numbers = [1,2,3,6,8,10,21,44]

newNumbers = [i for i in numbers if i%2==0]       # You can write conditionals like this in comphre.

newNumbers2 = [i if i%2==0 else "NO" for i in numbers]

print(newNumbers)
print(newNumbers2)


prodPrice = [1000, 2000, 3500, 0, 4000]
taxedPrice = [i*1.18 for i in prodPrice if i > 0]
print(taxedPrice)