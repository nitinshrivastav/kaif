def input():
    a=int(input("enter the number"))
    b=int(input("enter the value"))
    num=int(input("enter the choice"))
    return(a,b,num)     
             
def sum(a,b):
    return(a+b)
def minus(x,y):
    return(x-y)
def result():
    x,y,ch=input()
    if(ch==1):
        sum(x,y)
    else:
        minus(x,y)