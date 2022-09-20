# This codding is fruit store software
# list , loop , function 

menu1 = """
                WLCOME TO THE FRUIT MARKET 

            1). Manager
            2). Customer
            3). Exit
"""
menu2 = """
                Fruit Market Manager 

            1). Add fruit stock
            2). View fruit stock
            3). Update fruit stock
"""
fruit = {}
my_cart = {}

def fruit_manager ():
    print (menu2)

def add_fruit_stock ():
    print ("--------------ADD FRUIT STOCK-----------------")
    Fruit_name = input("Enter fruit name :")
    Qty = int(input("Enter fruit Qty (in kg) :"))
    price = int(input("Enter fruit price (per kg) :"))
    
    ddm['Qty'] = Qty 
    ddm['price'] = price 
    if Fruit_name in fruit:
        old_Qty = fruit[Fruit_name]["Qty"]
        fruit[Fruit_name] = ddm
    else:
        fruit[Fruit_name] = ddm

    print(fruit)


def view_fruit_stock ():
    print ("---------------Fruit Stock----------------------")                
    for k in fruit.keys():
        Qty = fruit[k]['Qty']
        price = fruit[k]['price']
        print(f" {k}  = {Qty}  = Rs.{price}/- ")
    else:
        print("----------------------------------- ")
    
    
def update_fruit_stock ():
    print ("----------------UPDATE FRUIT STOCK---------------------")
    for k in fruit.keys():
        Qty = fruit[k]['Qty']
        price = fruit[k]['price']
        print(f" {k}  = {Qty}  = Rs.{price}/- ")
    else:
        print("----------------------------------- ")

    Fruit_name = input("Enter fruit name :")
    Qty = int(input("Enter fruit Qty (in kg) :"))
    price = int(input("Enter fruit price (per kg) :"))
   
    ddm['Qty'] = Qty 
    ddm['price'] = price 
    if Fruit_name in fruit:
        old_Qty = fruit[Fruit_name]["Qty"]
        ddm['Qty'] = Qty 
        ddm['price'] = price
        fruit[Fruit_name] = ddm
    else:
        fruit[Fruit_name] = ddm

    print(fruit)

def customer_ac():
    total = 0 
    status = True 
    while status:
        ddm = {}
        print("-------------------  FRUIT  LIST  ---------------- ")
        for k in fruit.keys():
            price = fruit[k]['price']
            print(f" {k}  -  Rs. {price} ")
        else:
            print("----------------------------------- ")

        fruit_name = input("Enter product which you want to purchase : ")
        if fruit_name in fruit.keys():
            Qty = int(input("Enter no. of Qty do you want : "))
            main_Qty = fruit[fruit_name]["Qty"]
            if Qty<main_Qty:
                price = fruit[fruit_name]["price"]
                print("price will be : ",price*Qty)
                main_Qty -= Qty
                fruit[fruit_name]["Qty"] = main_Qty
                ddm['Qty'] = Qty # customer side Qty 
                ddm['price'] = Qty*price
                my_cart[fruit_name] = ddm
            else:
                print("stock not available")
        else:
            print("Product not available")
        choice = input("do you want more product : press 'y' for yes and press 'n' for no : ")
        if choice == 'y':
            status = True 
        else:
            print("-------------------  MY CART  ---------------- ")
            for k in my_cart.keys():
                Qty = my_cart[k]['Qty']
                price = my_cart[k]['price']
                total += price
                print(f" {k}  : {Qty} KG =  Rs.{price}/- ")
            else:
                print("---------------------------------------------- ")
                print(f" Total Bill : {total}")
            status = False

status = True
process = True
while status :
    print (menu1)
    Roll = int(input("Enter Your Roll :"))
    if Roll == 1:    
        print ("----------------------FRUIT MARKET MANAGER----------------------")    
        fruit_manager ()
        choice = int(input("Enter your choice :"))
        if choice == 1:
            while process :
                ddm = {}
                add_fruit_stock ()
                ch = input("do you want to add more fruit : press 'y' for yes and press 'n' for no : ")
                if ch=='y':
                    process = True
                else:
                    process = False
        if choice == 3:    
            update_fruit_stock ()
        elif choice == 2:
            view_fruit_stock ()
    elif Roll == 2:
        print ("---------------------------CUSTOMER---------------------")
        customer_ac ()
    else:
        print("---------THANK YOU FOR USING THIS APPLICATION  🙏 --------------")
        print("------------ VISIT AGAIN --------------------")
        status = False
    program_status = input("Do you want to go main menu : press 'y' for yes and press 'n' for no :  ")
    if program_status=='y':
        status = True
    else:
        status = False
        