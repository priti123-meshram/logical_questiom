# year=int(input("Enter year to be checked:")) 
# if(year%4==0 and year%100!= 0 or year%400==0): 
#     print("yes") 
# else: 
#     print("not")



# a=(input("enter the num"))
# if a>="a" and a<"z":
#     print("lower")
# elif a>="A" and a<="Z":
#     print("upper")
# # elif a>="a" or a<"z":
# #     print("alpha")
# else:
#     print("no")



# a= int(input('Please Enter the First Angle of a Triangle: '))
# b = int(input('Please Enter the Second Angle of a Triangle: '))
# c = int(input('Please Enter the Third Angle of a Triangle: '))

# # # checking Triangle is Valid or Not
# total = a + b + c

# if total == 180:
#     print("\nThis is a Valid Triangle")
# else:
#     print("\nThis is an Invalid Triangle")

# # Python Program to check Triangle is Valid or Not 1





# sub1=int(input("Enter marks of the first subject: "))
# sub2=int(input("Enter marks of the second subject: "))
# sub3=int(input("Enter marks of the third subject: "))
# sub4=int(input("Enter marks of the fourth subject: "))
# sub5=int(input("Enter marks of the fifth subject: "))
# avg=(sub1+sub2+sub3+sub4+sub5)/5
# if(avg>=90 and avg<=100):
#     print("Grade: A")
# elif(avg>=80 and avg<90):
#     print("Grade: B")
# elif(avg>=70 and avg<80):
#     print("Grade: C")
# elif(avg>=60 and avg<70):
#     print("Grade: D")
# else:
#     print("Grade: F")




# # calculate its Gross salary according to following:
# If Basic Salary <= 15000, then HRA = 25% of Basic Salary, DA = 80%
# of Basic Salary
# If Basic Salary <= 25000, then HRA = 30% of Basic Salary, DA = 90%
# of Basic Salary
# If Basic Salary > 25000, then HRA = 35% of Basic Salary, DA = 95%
# of Basic Salary
# Gross Salary = Basic Salary + HRA + DA
# Also show the output.​

# basic_salary = int(input("Enter your basic salary: "))

# if basic_salary > 25000:

#    hra = .35 * basic_salary

#    da = .95 * basic_salary

# elif basic_salary > 15000:

#    hra = .30 * basic_salary

#    da = .90 * basic_salary

# else:

#    hra = .25 * basic_salary

#    da = .80 * basic_salary

# gross_salary = basic_salary + hra + da

# print("The gross salary is gross_salary.",gross_salary)



# n = input("Input the Filename: ")
# a = n.split(".")
# print ("The extension of the file is : " ,a[-1])





# name = input("Enter your first name and last: ")
# i = 0
# for index in name:
#     if index != " ":
#         i += 1
#     else:
#         last = name[i+1:]
#         first = name[0:i]
# print (last + " " + first)


# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))


# a=input("enter the num")
# if a>="a" and a<="z":
#     # b='ing'.join(a)
#     print(a+"ing")
# else:
#     print("jhgf")




# from ast import AnnAssign


# def add_string(str1):
#     length = len(str1)
#     if length > 2:
#         if str1[-3:] == 'ing':
#             str1 += 'ly'
#     else:
#         str1 += 'ing'
#     print(str1)
# add_string('ting')



# str1=input("enter the num")
# length = len(str1)
# if length > 2:
#     if str1[-3:] == 'ing':
#         str1 += 'ly'
# else:
#     str1 += 'ing'
#     print(str1)




# yyyy=int(input("enter the year"))
# mm=int(input("enter the month"))
# dd=int(input("enter the date"))
# if yyyy>=2001 and yyyy<=2022:
#     if mm<=12:
#         if dd<=31:
#             print(yyyy,"/",mm,"/",dd+1)
# else:
#     print("not")



# yyyy=int(input("enter the year"))
# mm=int(input("enter the month"))
# dd=int(input("enter the date"))
# if yyyy>=2001 and yyyy<=2022:
#     if mm<=12:
#         if dd<=31:
#             print(yyyy,"/",mm,"/",dd+1)
# else:
#     print("not")



# a=int(input("enter the num"))
# i=1
# while i<=10:

#     print(a,"x",i, " =  ",a*i)
#     i=i+1


# a=int(input("enter the num"))
# i=a
# while i>=1:
#     print(i)
#     i=i-1
# print(i)
    

# n=[8,9,6,7,-5,-3,-6,-9,3,7,9]
# a=[]
# i=0
# while i<len(n):
#     b=n[i]
#     if b<0:
#         a.append(1)
#     elif b>0:
#         # print(i)
#         a.append(b)
#     i=i+1
# print(a)



# num=int(input("enter the num"))
# i=0
# while i<num:
#     print(num%100)
#     # break
#     i+=1
    # break




# fabonic=int(input("enter the num"))
# a=0
# b=1
# index=0
# while index<=fabonic:
#     print(index)
#     a=b
#     b=index
#     index=a+b
    




# a=int(input("enter the number: "))
# i=0
# while i<a:
#     if a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0:
#         print("prime")
#     elif a==2 or a==3 or a==5 or a==7:
#         print("prime")
#     else:
#         print("not prime") 
#     i+=1


# n=[1,0,2,0,0,1,1,1]
# a=[]
# a=[]
# c=0
# for i in range(len(n)):
#     if n[i]==0:
#         c=c+1
#         a.append(c)
#     else:
#         a.append(0)
# print(a)
    





# n=[1,0,2,0,0,1,1,1,0]
# a=[]
# c=0
# i=0
# while i <len(n):
#     if n[i]==0:
#         c=c+1
#         a.append(c)
#     else:
#         a.append(0)
#     i=i+1
# print(a)
    





# n=int(input("enter the num"))
# i=(n)
# rev=0
# while i>0:
#     remainder=i%10
#     i//=10
#     rev=rev*10+remainder
# if n==rev:
#     print("it is palindrome",n)
# else:
#     print("it is not palindrome",n)







# list1=["mom","dad","pooja","priti"]
# i=0
# c=0
# while i<len(list1):
#     m=list1[i][::-1]
#     if list1[i]==m:
#         c=c+1
#     i=i+1
# print(c)



# n=int(input("enter"))
# i=0
# while i<=n:
#     a=i%10
#     i=i+1
# print(a)