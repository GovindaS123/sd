a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    mod=a%b
    return sum,sub,mul,mod
r1,r2,r3,r4=cal(a,b)
print(r1)
print(r2)
print(r3)
print(r4)
def employee_name():
    return "g","o","v"
g,o,v=employee_name()