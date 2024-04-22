#guessing number game
import random as r

n=int(input("enter the number "))
c=r.randrange(1,n)
y=int(input("enter the number "))
while(True):
    if(y==0):
        print("game over,player quite the game.")
        break
    elif(y==c):
        print("congratulation you are right. the random number was:",c)
        break
    elif(y<c):
        y=int(input("you are near to correct it play some more time"))
    elif(y>c):
        y=int(input("your guessing is around to corect.please play more time"))
    else:
        y=int(input("try again"))
        