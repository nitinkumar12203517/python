
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def pow(a):
    return a**2
def floordiv(a,b):
    return a//b
def squareroot(a):
    return a**a
a=int(input())
b=int(input())
operation=int(input())
if operation==1:
    print(div(a,b))
elif operation==2:
    print(mod(a,b))
elif operation==3:
    print(pow(a))
elif operation==4:
    print(floordiv(a,b))
else:
    print(squareroot(a))
