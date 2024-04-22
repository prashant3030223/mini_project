#grading system 
name=input("enter the name of student ")
p1=int(input("enter the first subject marks "))
p2=int(input("enter the second subject marks "))
p3=int(input("enter the marks of third subject "))
p4=int(input("enter the marks of forth subject "))
p5=int(input("enter the marks of fifth subject "))
t=p1+p2+p3+p4+p5
percentage=t/5
print("your percentage is:",percentage)
if(p1>100 or p2>100 or p3>100 or p4>100 or p5>100 or p1<0 or p2<0 or p3<0 or p4<0 or p5<0):
    print("enter the wrong marks criteria")
elif(percentage==100):
    print("grade==O")
elif(percentage>=90):
    print("grade==A+")
elif(percentage>=80):
    print("grade==B+")
elif(percentage>=70):
    print("grade==B")
elif(percentage>=60):
    print("grade==C")
elif(percentage>=50):
    print("grade==D")
else:
    print("the student is fail")

