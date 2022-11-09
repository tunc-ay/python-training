# q1 > get product info. dictionary list. when completed, list information with the while loop.

products = {}
x = int(input("Enter number of products: "))
i = 0
while i < x:
    prodId = input("Enter product id: ")
    prodName = input("Enter name: ")
    prodPrice = input("Enter price: ")
    products[prodId] = {
    "prodName": prodName,
    "prodPrice": prodPrice
}
    i += 1
print(products)

