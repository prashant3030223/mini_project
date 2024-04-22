#reverse forward row,column printing
s=int(input("enter the starting point "))
e=int(input("enter the end point "))
u=int(input("enter the updation "))

choice=input("enter your choice for forward printing or reverse printing:")
choice2=input("enter the choice for row printing or column printing:")

if choice=="farward":
    if choice2=="row":
        for i in range(s,e,u):
            print(i,end=',')
    elif choice2=="column":
        for i in range(s,e,u):
            print(i)
    else:
        print("second choice is not correct. enter the valid choice.")
elif choice=="reverse":
    if choice2=="row":
        for i in range(e,s,-u):
            print(i,end=',')
    elif choice2=="column":
        for i in range(e,s,-u):
            print(i)
    else:
        print("second choice is not correct. enter a valid choice")
else:
    print("your both choices are wrong")