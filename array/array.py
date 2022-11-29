
#i have used dictionary in python  programming langue
product = {
    'bike':100,
    'TV':200,
    'Album':10,
    'book':5,
    'phone':500,
    'computer':1000,}

    #Filter and show the product that will be bought when you don't have much money I mean Cheap one
print("\n")
print("product to buy when i have little money")
print(dict(filter(lambda x : x[1] == 10,product.items())))

#Filter and show the product that will be expensive in the array
print("\n")
print("expensive product")
print(dict(filter(lambda x : x[1] == 1000,product.items())))
#Calculate the full price of all product combined
print("\n")
print("summation of all")
print(sum(product.values()))
#Calculate the full price of all product combined and remove product that are under the 10 dollar
print("\n")
print("summation of all by removing these under 10")
del product['book']
print(sum(product.values()))










    
    
