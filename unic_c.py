# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.


input_list = [1, 2, 2, 5, 8, 4, 4, 8]
c=0
a=[]
for i in input_list:
    if i not in a:
        a.append(i)
        c=c+1
print(c, a)




