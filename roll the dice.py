#roll the  dice
import random as r
i=1
s1=s2=0
while(i<7):
    c=r.randint(1,6)
    y=int(input("enter the number between 1to 6: "))
    choice=input("if you quite type'quite' otherwise type 'n' : ")
    s1+=c
    s2+=y
    if(choice=='quite'):
        break
    elif(choice=='no'):
        continue
    else:
        print("wrong choice")
        break
        
print("\n")
print("your score is:",s2)
print("the computer score is:",s1)
print("\n")
if(s1>s2):
    print("computer won with score of:",s1)
else:
    print("you won with the score of:",s2)
