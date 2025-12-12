a=int(input())
ans=[]
b=1
n=1
while n<=a:
    if n%2==1:
        ans.append(b)
        b+=2
    n+=1
print(ans)