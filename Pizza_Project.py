'''
#Pizza delivery
1. Admin
    1.1 login/logout
    1.2 Stock management
    1.3 View stock
2. Customer
    2.1 login/logout
    2.2 Order
    2.3 Menu

if the product stock is empty then the user cannot order that product
there should be atleast 3 products
'''
aid = "Admin"
apswd = 1234
cid = "Customer"
cpswd = 1234
pizza = 5
fries = 5
cold_drink = 5
while(True):
    print("\n\n\t\t\t\t Press 1 for Admin panel\n"
          "\t\t\t\tPress 2 for Customer panel\n"
          "\t\t\t\tPress 3 to quit the App")
    choice = int(input("Enter your choice"))
    if choice==1:
        print("Admin Panel")
        adminid = input("\n\t\t\t\t Please enter you id")
        if adminid==aid:
            adminpass = int(input("\n\t\t\t\t Please enter your password"))
            if adminpass==apswd:
                print("\n\t\t\t\t Welcome admin")
                while(True):
                    print("\n\t\t\t\tMain Menu")
                    print("\n\t\t\t\tType 'View' to see the stock"
                          "\n\t\t\t\tType 'Manage' for stock management"
                          "\n\t\t\t\tType 'Logout' to logout of the panel")
                    adminfun = input("\n\t\t\t\t Please enter your choice")
                    if adminfun=="View":
                        print("\n\t\t\t\tThis is the stock available")
                        while(True):
                            print("\n\t\t\t\t We have ",pizza," pizzas left"
                                  "\n\t\t\t\t We have ",fries," fries left"
                                  "\n\t\t\t\t We have ",cold_drink," cold drink left")
                            escview = input("Press 0 to go back")
                            if escview=="0":
                                break

                    elif adminfun=="Manage":
                        print("\n\t\t\t\tThis is the stck management panel")
                        while(True):
                            print("\n\t\t\t\t Type 'Add' to add stocks and 'Del' to delete stcoks"
                                  "\n\t\t\t\t Type 'Back' to go back to the main menu")

                            stckmng = input("Enter your choice").capitalize()
                            if stckmng=='Add':
                                print("\n\t\t\t\t Add the number of pizzas")
                                pizzaadd = int(input())
                                pizza+=pizzaadd
                                print("\n\t\t\t\t Add the number of fries")
                                friesadd = int(input())
                                fries += friesadd
                                print("\n\t\t\t\t Add the number of cold drink")
                                coldadd = int(input())
                                cold_drink += coldadd
                            elif stckmng=="Del":
                                print("\n\t\t\t\t Delete the number of pizzas")
                                pizzadel = int(input())
                                if pizzadel>pizza:
                                    print("\n\t\t\t\t We have only ",pizza," is the stock")
                                else:
                                    pizza-=pizzadel
                                print("\n\t\t\t\t Delete the number of fries")
                                friesdel = int(input())
                                if friesdel > fries:
                                    print("\n\t\t\t\t We have only ", fries, " is the stock")
                                else:
                                    fries -= friesdel
                                print("\n\t\t\t\t Delete the number of cold drink")
                                cdel = int(input())
                                if cdel > cold_drink:
                                    print("\n\t\t\t\t We have only ", cold_drink, " is the stock")
                                else:
                                    cold_drink -= cdel
                            elif stckmng=="Back":
                                break
                    elif adminfun=="Logout":
                        print("\n\t\t\t\tYou have successfully logged out")
                        break


            else:
                print("\n\t\t\t\t Wrong Password")
        else:
            print("\n\t\t\t\t Wrong ID")
    elif mainchoice==2:
        print("Customer Panel")
        customerid = input("\n\t\t\t\t Please enter you id")
        if customerid==cid:
            customerpass = int(input("\n\t\t\t\t Please enter your password"))
            if  customerpass== cpswd:
                print("\n\t\t\t\t Welcome Customer")
                while (True):
                    print("\n\t\t\t\tMain Menu")
                    print("\n\t\t\t\tType 'Menu' for the menu"
                          "\n\t\t\t\tType 'Order' to order"
                          "\n\t\t\t\tType 'Logout' to logout of the panel")
                    customerfun = input("\n\t\t\t\t Please enter your choice")
                    if customerfun == "Menu":
                        print("\n\t\t\t\tGLA Pizza Menu")
                        while (True):
                            print("\n\t\t\t\t Pizza....................10rs"
                                  "\n\t\t\t\t Cold Drink...............5rs"
                                  "\n\t\t\t\t Fries....................2rs")
                            escview = input("Press 0 to go back")
                            if escview == "0":
                                break

                    elif customerfun == "Order":
                        print("\n\t\t\t\tPlease order ")
                        while (True):
                            print("\n\t\t\t\tPress 1 for pizza"
                                  "\n\t\t\t\tPress 2 for cold drink"
                                  "\n\t\t\t\tPress 3 for fries"
                                  "\n\t\t\t\tPress 0 to go back to the main menu")
                            order = int(input())
                            if order==1:
                                while(True):
                                    print("\n\t\t\t\t How many pizzas do you want to order"
                                          "\n\t\t\t\t Press 0 to go back to the main menu")
                                    pizzaorder= int(input())
                                    if pizza<pizzaorder:
                                        print("\n\t\t\t\tWe have only ",pizza," only")
                                    elif pizzaorder==0:
                                        break
                                    else:
                                        pizza-=pizzaorder
                                        print("\n\t\t\t\tOrder confirmed")
                            elif order==2:
                                while (True):
                                    print("\n\t\t\t\t How many cold drinks do you want to order"
                                          "\n\t\t\t\t Press 0 to go back to the main menu")
                                    coldorder = int(input())
                                    if coldorder < coldorder:
                                        print("\n\t\t\t\tWe have only ",cold_drink, " only")
                                    elif coldorder==0:
                                        break
                                    else:
                                        cold_drink-=coldorder
                                        print("\n\t\t\t\tOrder confirmed")
                            elif order==3:
                                while (True):
                                    print("\n\t\t\t\t How many fries do you want to order"
                                          "\n\t\t\t\t Press 0 to go back to the main menu")
                                    fryorder = int(input())
                                    if fries < fryorder:
                                        print("\n\t\t\t\tWe have only ",fries, " only")
                                    elif fryorder==0:
                                        break
                                    else:
                                        fries -= fryorder
                                        print("\n\t\t\t\tOrder confirmed")
                            elif order==0:
                                break


                    elif customerfun == "Logout":
                        print("\n\t\t\t\tYou have successfully logged out")
                        break


            else:
                print("\n\t\t\t\t Wrong Password")
        else:
            print("\n\t\t\t\t Wrong ID")
    elif mainchoice==3:
        print("Thankyou for using the App")
        break
    else:
        print("Wrong choice")