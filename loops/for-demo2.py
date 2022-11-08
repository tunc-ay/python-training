products = [
    {'prodName': 'iPhone 8', 'prodPrice': '550'}, 
    {'prodName': 'iPhone 8 Plus', 'prodPrice': '650'}, 
    {'prodName': 'iPhone X', 'prodPrice': '750'},
    {'prodName': 'iPhone XR', 'prodPrice': '550'}, 
    {'prodName': 'iPhone 11', 'prodPrice': '650'}, 
    {'prodName': 'Samsung S10', 'prodPrice': '750'}
]

# q1 > list all items
# for prod in products:
#     print(prod)

# q2 > sum of all items' price
# sum = 0
# for product in products:
#     sum = sum + int(product['prodPrice'])
# print(sum)

# q3 > list of thos items lower than 6000
# for product in products:
#     if int(product['prodPrice']) < 600:
#         print(product['prodPrice'])

# q4 > get price information based on prodName
prodSearch = input("Please enter phone name: ")
for prod in products:
    if prod['prodName'].find(prodSearch.lower()) > -1:
        print(prod['prodName'])



