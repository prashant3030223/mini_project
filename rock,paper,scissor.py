#rock paper scissor
import random as r
c=r.choice(['rock','scissor','paper'])
y=input("choice only one 'rock,papr,scissor':")
if(y=='rock'):
    if(c=='rock'):
        print("match draw")
    elif(c=='paper'):
        print("computer wins")
    elif(c=='scisor'):
        print("you win")
if(y=='scissor'):
    if(c=='scisor'):
        print("match draw")
    elif(c=='rock'):
        print("computer wins")
    elif(c=='paper'):
        print("you wins")
if(y=='paper'):
    if(c=='paper'):
        print("match draw")
    elif(c=='rock'):
        print("we loose")
    elif(c=='scissor'):
        print("we win")
    else:
        print("nobody wins")
    