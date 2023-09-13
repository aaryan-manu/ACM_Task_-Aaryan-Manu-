
t = int(input(""))
L=[]
for a in range(t):
    sum=0
    n=int(input("Enter number: "))
    for i in range(n):
        if i%3==0 or i%5==0:
            sum+=i
    
    L.append(sum)
for i in L:
    print(i)
