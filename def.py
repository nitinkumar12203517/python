def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
a=int(input())
b=int(input())
operation=int(input())
if operation==1:
    print(add(a,b))
elif operation==2:
    print(subtract(a,b))
else:
    print(multiply(a,b))