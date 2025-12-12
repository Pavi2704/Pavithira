a={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
ans=list(map(int, input().split()))
for i in range(1,10):
    for j in ans:
        if j%i==0:
            a[i]+=1
print(a)