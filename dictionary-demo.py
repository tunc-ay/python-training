# Q1 > create dictionary with input from users

products = {}

prodId = input("Enter id: ")
prodName = input("Enter name: ")
prodPrice = input("Enter price: ")

products[prodId] = {
    "prodName": prodName,
    "prodPrice": prodPrice
}

prodId = input("Enter id: ")
prodName = input("Enter name: ")
prodPrice = input("Enter price: ")

products[prodId] = {
    "prodName": prodName,
    "prodPrice": prodPrice
}

prodId = input("Enter id: ")
prodName = input("Enter name: ")
prodPrice = input("Enter price: ")

products[prodId] = {
    "prodName": prodName,
    "prodPrice": prodPrice
}

print(products)

# Q2 > provide info to users upon inquiry

product = {
    '1': {'prodName': 'Samsung S10', 'prodPrice': '550'}, 
    '2': {'prodName': 'Samsung S11', 'prodPrice': '650'}, 
    '3': {'prodName': 'Samsung S12', 'prodPrice': '750'}
}

prodId = input("Enter an id: ")
prod = product[prodId]
print(prod)