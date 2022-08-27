menu = """

                MENU 

        JAYBHAVANI 

        VADAPAV    30
        DABELI     30
        BHEL       65
    """

print(menu)
product_list = [] 
price_list = [] 
status =True

name = input("Enter your name : ")
while status:
    product = input("Enter product which you want : ")
    product_list.append(product)
    if product=="VADAPAV" or product=="DABELI":
        price = 30
    else:
        price = 65
    qty = int(input("Enter no. of qty do you want ? "))
    total_price = qty * price
    price_list.append(total_price)
    print(total_price)

    choice = input("do you want more product : press y for yes and press n for no : ")
    if choice=="y":
        status = True 
    else:
        status = False

count = 0 
for product in product_list:
    print(f"{product} = {price_list[count]}")
    count+=1 

print("TOTAL PRICE = ",sum(price_list))