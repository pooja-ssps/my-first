def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a*b
def div(a,b):
    return a/b

while True:

    select =input("add,sub,mul,div=")

    if select in ('add','sub','mul','div'):
        num1 = int(input("enter a number="))
        num2 = int(input("enter a number="))
    if select == 'add':
        print(num1, "+", num2, "=", add(num1, num2))
    elif select =='sub':
        print(num1,"-",num2,"=",sub(num1,num2))
    elif select == 'mul':
        print(num1,"*",num2,mul(num1+num2))
    elif select =='div':
        print(num1,"/",num2, div(num1,num2))
        break
    else:
        print("invalid")

