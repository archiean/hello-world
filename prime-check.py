n=int(input("Enter a number"))
x=n%2
if x==0:
    print("Not prime")
if n==45:
    print('45')
    
while x>0:
    for c in range(3,n):
        if n==45:
            print('45')
            break
        if(n%c)==0:
            print("Not prime")
            
            break
    else:
        print("Is prime")
        break
