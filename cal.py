n1=float(input("enter first number :"))
n2=float(input("enter second number :"))
operation=input("enter operation '+' or '-' or '*' or '/' :")
if operation=="+":
    print(n1+n2)
elif operation=="-":
    print(n1-n2)
elif operation=="*":
    print(n1*n2)
elif operation=="/":
    print(n1/n2)
else:
    print("invalid operation")