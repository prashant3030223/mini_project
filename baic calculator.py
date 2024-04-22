#basic calculator 
x=int(input("enter the number "))
y=int(input("enter the number "))
choice=input("enter your choice,'add','substract','multiply','divide'")
if(choice=='add'):
    a=x+y
    print("the addition of number:",a)
elif(choice=='substrsct'):
    s=x-y
    print("the substraction of number:",s)
elif(choice=='multiply'):
    f=x*y
    print("the number is multiplied:",f)
elif(choice=='divide'):
    d=x//y
    print("the number is divided:",d)
else:
    print("wrong choice")