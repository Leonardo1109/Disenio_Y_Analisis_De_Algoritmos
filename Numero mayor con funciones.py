a=13
b=8
c=15

def max2(a,b):
    if a>b:
        return a
    else:
        return b

def max3 (a,b,c):
    return max2(a,max2(b,c))

print(max3(a,b,c))
print("//")
print (max2(a,max2(b,c)))
