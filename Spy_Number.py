num=int(input())
p=1
k=0
while num>0:
        r=num%10
        k=k+r
        p=p*r
        num=num//10
        
if p==k:
    print("Spy Number")
    
else:
    print('Not Spy Number')