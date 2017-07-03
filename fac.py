# factors of a number
a=2639
f=[]
for i in range(3,a,2):
    if a%i==0:
        f.append(i)
#print(f)
b=max(f)
p=[]
l=len(f)



for j in range(l):
    #print(f[j])
    
    for c in range(3,f[j],2):
        #print(f[j],c)
        if f[j]%c==0:
            #print(f[j],'%',c,'==0')
            break
    else:
        #print(f[j],c)

        p.append(f[j])
            
#print(p)
g=max(p)
print(g)


        
