n=[1,3,6,8,9,7,5,4,2,9,2,2,2,2]
a=[]
for i in n:
    if i not in a:
        a.append(i)
print(a)