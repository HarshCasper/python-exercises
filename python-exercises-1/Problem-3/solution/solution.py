x=[int(x) for x in input().split()]
x1=sorted(x)
c=0
for i in range(len(x)):
    if x[i]==x1[c]:
        c=c+1
print(len(x)-c,end="")