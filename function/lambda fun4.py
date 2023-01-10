#plusone=lambda n:n+1
#print(plusone(10))
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(10,20))
max=lambda a,b:a if a>b else b
print(max(100,300))