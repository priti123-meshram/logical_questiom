# list1=["mom","dad","pooja","priti"]
# i=0
# c=0
# while i<len(list1):
#     m=list1[i][::-1]
#     if list1[i]==m:
#         c=c+1
#     i=i+1
# print(c)





# n="priti"
# c=list(n)
# b=[]
# i=1
# while i<=len(n):
#     b.append(n[-i])
#     i+=1
# if c==b:
#     print("it is polindrome ",b)
# else:
#     print("not",b)





i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1

