inventory={}
while True:
    action= input("enter what want you to do? add, remove, display,quit: ")
    if action=='add':
        item=input("enter item name: ")
        quantity=int(input("enter your quantity: "))
        if item in inventory:
            inventory[item]+=quantity
        else:
            inventory[item]=quantity
    elif action=='remove':
        item=input("enter the name of item you want to remove: ")
        quantity=int(input("enter the quantity you want to remove: "))
        if item in inventory and inventory[item]>=quantity:
            inventory[item]-=quantity
        elif item in inventory and inventory[item]<quantity:
            print(f"There are only {inventory[item]} left in {item} left in inventory.")
        else:
            print("ther is no item left in inventory.")
    
    elif action=='display':
        print("Inventory")
        for key,value in inventory.items():
            print(f"{key}:{value}")
    
    elif action =='quit':
        break
    else:
        print("invalid entry please try again. ")