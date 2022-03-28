a=[1,2,3,10,12,15]
i=1
c=0
# while i<len(a):
#     if(i%2!=0):
#         if(a[i]%2!=0):
#             c+=1
#             # print(
for i in range(len(a)):
    if i%2!=0:
        if (a[i]%2!=0):
            print(c)
        c+=1
    i+=1






