# def add (x,y,z):
#     if x>y and x>z:
#         print(x)
#     elif y >y and y>z:
#         print(y)
#     else:
#         print(z)
# add(2,6,9)

# def sum():
#     list=[8,2,3,0,7]
#     i=0
#     sum=0
#     while i<len(list):
#         sum=sum+list[i]
#         i=i+1
#     print(sum)
# list=[8,2,3,0,7]
# sum()
#     sum=0
#     for i in list:
#         sum=sum+i
#     print(sum)
# sum()




# def add():
#     n=[8, 2, 3, -1, 7]
#     i=0
#     m=1
#     while i <len(n):
#         m=m*n[i]
#         i=i+1
#     print(m)
# add()

# def str():
#     str="1234abcd"
#     i=1
#     # a=[]
#     while i<=len(str):
        # a.append(str[-i])

#         print(str[-i],end=" ")
#         i=i+1
# str()



# def add(i):
#     if i in range(1,20):
#         print(i,"in range")
#     else:
#         print(i,"not in range")
# add(5)



# def u_l(str):
#     u=0
#     l=0
#     for i in str:
#         if i. islower():
#             l=l+1
#         elif i.upper():
#             u=u+1
#     return("upper:",u,"lower:",l)
# print(u_l("The quick Brown Fox"))



def add():
    n=[4,6,7,7,6,6,7,8,6,5,5,4,4,3]
    a=[]
    for i in n:
        if i not in a:
            a.append(i)
    print(a)
add()