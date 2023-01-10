a=int(input("Enter the fact number:"))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
result=fact(a)
print(result)