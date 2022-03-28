# o/p:  [[2,1],2,3,[2,4],5,1]



n=[1,8,2,3,4,4,5,1]
a=[]
i=1
while i<len(n):
    # if n[i]+n[i]==number:
    k=[n[i],n[i]]
    if k not in a:
        a.append(k)
    i=i+1
print(a)
