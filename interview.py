n='w3resource'
a = {} 
for i in n:
    if i in a: 
        a[i]=a[i]+1
    else:
        a[i] = 1 
for j in a:
    print(j,':',a[j])

# n='w3resource'
# b=len(n)
# # print(b)
# a=[]
# c=0
# for i in n:
#     for j in i:
#         if j not in a:
#             a.append(j)
# print(a)


# n = "w45ert5yt5wwww" 
# a=[]
# for i in n:
#     if i not in a:
#         a.append(i)
# print(a)
# i=0
# while i<len(a):
#     count=0
#     for j in range(0,len(n)):
#         if a[i]==n[j]:
#             count=count+1
#     print(a[i], "=",count)
#     i=i+1



# import json
# k={"name":"priti",
#     "place": "rasa"
#     }
# with open("priti.json","r")as file:
#     b=json.load(file,)
#     print(k)


    










# a=2+5j
# b=3+2j
# print(a*b)



# a=not(11 and 12 or 23 and 34)
# print(a)