# List product excluding duplicates.
#     List = [6,1,3,5,6,3,1]
#     Output: 60

#list ki sum nikalke usko 4 se multiplae kar derna hai.

n = [6,1,3,5,6,3,1]
a=[]
sum=0
for i in n:
    if i not in a:
        # sum=sum+i
        a.append(i)
        sum=sum+i
print(sum*4)