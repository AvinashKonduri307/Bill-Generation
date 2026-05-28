from datetime import datetime

Name = input("Enter your name: ")
print("Welcome to the SuperMArt, " + Name + "!")
# List of items available in the supermarket
lists = '''
1. Milk      RS 78/Litre
2. Eggs      RS 120/Dozen
3.Rice       RS 60/Kg
4.Bread      RS 40/Loaf
5.Butter     RS 150/Kg
6.Cheese     RS 200/Kg
7.Fruits     RS 100/Kg
8.Vegetables RS 50/Kg
9.Meat       RS 300/Kg
10.Fish      RS 250/Kg
11.Snacks    RS 50/Packet
12.Beverages RS 80/Bottle
'''
#declaration of variables
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

#rates for items
rates = {
    1: 78,
    2: 120,
    3: 60,
    4: 40,
    5: 150,
    6: 200,
    7: 100,
    8: 50,
    9: 300,
    10: 250,
    11: 50,
    12: 80
}
option = int(input("Do you want to see the list of items available in the SuperMart? (1 for yes, 0 for no): "))
if option == 1:
    print(lists)
else :
    print("Thank you for Visiting the SuperMart, " + Name + "!")
    exit()
for i in range(len(rates)):
    item = int(input("Enter the item number you want to buy (0 to stop): "))
    if item == 0:
        break
    quantity = int(input("Enter the quantity: "))
    if item in rates:
        price = rates[item] * quantity
        pricelist.append(price)
        totalprice += price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
    else:
        print("Invalid item number. Please try again.")
print("Calculating the total price...")
print("Total price: Rs " + str(totalprice))
discount = 0
if totalprice > 1000:
    discount = totalprice * 0.1
    print("You have received a 10% discount of Rs " + str(discount))
Finalprice = totalprice - discount
print("Final price after discount: Rs " + str(Finalprice))
print("Generating receipt...")
print("SuperMart Receipt")
print("Name: " + Name)
print("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Items Purchased:")
for i in range(len(ilist)):
    print("Item " + str(ilist[i]) + " - Quantity: " + str(qlist[i]) + " - Price: Rs " + str(plist[i]))
print("Total Price: Rs " + str(totalprice))
print("Discount: Rs " + str(discount))
print("Final Price: Rs " + str(Finalprice))
print("Thank you for shopping at SuperMart, " + Name + "!")

