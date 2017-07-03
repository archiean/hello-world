a=1
b=2
s=0
a,b=b,a+b

while a<4000000:
    if a%2==0:
        s=s+a
    a,b=b,a+b
print(s)
