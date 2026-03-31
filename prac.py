# def any_power(n):                    #so the n is taken for the power of any number
#     def any_number(x):               #and x is taken for the number what u want to multiply it 
#         return x**n
#     return any_number
# cube=any_power(10)
# print(cube(8))            

# def square(a):
#     return a**3
# print(square(42))

# DECORATOR---------------------------------

# decoretor item is mainly used for enhancing the functionality of other function
# WE USE @ AS A DECORATOR to call the function
# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def warppe_function(*args,**ka):
#         '''wrapper function'''
#         print("this is awasome")
#         return any_function(*args,**ka)
#     return warppe_function



# @decorator_function
# def fun():
#     print("this is very good")
# fun()
# @decorator_function
# def add(*s):
#     ''' this is add function'''
#     return (s)


# print(add.__doc__)
# print(add.__name__)
# print(add(1,2,51,21,41554,45,54,54,54,545,4,))

# # def add_all(*args):
#     total=0
#     for i in args:
#         total+=i
#     return [total]
# print(add_all(1,5,1,4,41,4,4,4,4,4,))    #so it is normal if we pass list then inside the tuple
#the it is comming error like       print(add_all(1,5,1,4,41,[4,4,4,4,4]))
#to slove that 
# we can use  the decoreter item
# that is it will take only int only and not any data type 
# from functools import wraps
# def only_int_allows()
# from functools import wraps
# def only_int(funce):
#     @wraps(function)
#     def warper(*y,**u):
#         if all([type(y)==int for i in y]):
#             return funce(*y,**u)
#         return "invild"
#         # data_types=[]
#         # for i in y:
#         #     data_types.append(type(y)==int)
#         # if all (data_types):
#         #     return funce(*y,**u)
#         # return ("invild")
#     return warper
# # # def add_all(*args):
# #     total=0
# #     for i in args:
# #         total+=i
# #     return [total]
# # print(add_all(1,5,1,4,41,4,4,4,4,4,))          
#     

# #  MAKING A DISCOUNT FOR ANY LAPTOP 

# class Laptop:
#     discount=50
#     def __init__(self,brand,model_name,price):
#         self.brand= brand
#         self.name=model_name
#         self.price=price
#         self.laptop_fulllname=brand+" "+model_name
    
#     def discount_any_laptop(self,):
#         offers=self.price*(Laptop.discount/100)
#         return self.price-offers
# # lap3=Laptop(f"asus","adggjhd252124",{200})
# lap1=Laptop("hp","asd4512124",100)
# lap2=Laptop("dell","65245sdfs",40000)    
# print(lap1.discount_any_laptop())
# print(lap1.__dict__)
# print(lap2.brand)
# # def mai in tgeh tg ergfbhjjggd
# # bfgfg fo i in loppp 
# # ra
# x = 5
# while x > 0:
#     print(x, end="")
#     x -= 1


# num=int(input())
# i=0
# while i in range(1,num):
#      i**num
#      i+=1
#      print(i) 
# for i in range(1,10):
#     print(f"hello world: {i}")
# num=int(input())
# i = 1
# while i < num+1:
#     print(i**2,end="")
#     i += 1


# num=int(input())
# factor=1
# while num>0:   #num is greater then zero then only the condition will be true
#     factor*=num     #factor=factor* num(5) #1*5,4*1,3*1,2*1
#     num-=1                   
# print(factor)

# num = int(input())
# factorial = 1

# while num > 0:
#     factorial *= num
#     num -= 1

# print(factorial)
# word=input()
# vowel=0
# i=0
# while i<len(word):
#     v=word[i]
#     if v=="a"or  v=="e"or v=="a"or v=="o" or v=="u":
#         vowel+=1
#     i+=1    
# print(vowel)    
# word = input("Enter a word: ")
# vowel = 0
# # i = 0
# vowel=0
# i=0
# while i < len(word):
#     v = word[i].lower()  # Convert the character to lowercase
#     if v in "aeiou":
#         vowel += 1
#     i += 1
# print(vowel)
# class mobile:
#     def __init__(self,name):
#         self.name=name
# class store:
#     def __init__(self):
#         self.mobile=[]
#     def add_mobile(self,new_mobile):
#         self.mobile.append(new_mobile)
# oneplus=["oneplus"]
# print(mobile(oneplus))

# soham salary is 100

# subham salray is 200
#how to read file in python 
# with open('file.txt','r') as t:
#     with open("salary.txt",'a')as q:
#         for i in t.readlines():
#             name,salary=i.split(",")
#             q.write(f"{name} salary is {salary}") 


# from csv import DictReader
# with open('file.csv','r') as f:
#     csv=DictReader(f)
#     for i in csv:
#         print(i['number'])
# from csv import DictReader,DictWriter:
# with open('file.csv')
# import array as arr

# # Creating an array of integers
# numbers = arr.array('i', [1, 2, 3, 4, 5])

# # Function to calculate the sum of array elements
# def array_sum(array):
#     total = 0
#     for num in array:
#         total += num
#     return total

# # Calculating and printing the sum
# print("Sum of array elements:", array_sum(numbers))



# def add(a,b):
#     return a**b
# print(add(4,108))    
# dsa
# -________________________________________________________________________

# a= int(input (""))
# # b=input("")
# # c=a
# # a=b
# # b=c
# # print(f"so a is {a},and b is {b}")
# if (a%2==0):
#     print("even")
# else:    print("odd")

# multiplication table__________________________
# num= int(input(""))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")
# ________________-----------------------------------------
# a,b,c=map(int(input("").split( )))#map is used to take multiple input in one line and split is used to split the input by space and then it will be converted into int by map
# if a>b and a>c:
#     print(f"{a}this is the largest number ")
# elif b>a and b>c:
#     print(f"{b}is the max num")
# else :
#     print(f"{c}i the max num ")

# def celcius_fahern(c):
#     return (c*9/5)+32
# c=int(input())
# print(celcius_fahern(c))


#find the  max number in the list  not uing max function 

# arr=[4,12,1,5,1,4,5,7,2,74,6,8,5,5,8]
# max_num = arr[0]
# for i in arr:
#     if i>max_num:
#         max_num=i
# print(max_num)
#----------------------------------------------------------------------
# reverse an array
# arr=[1,2,3,4,5,6,7,8,9]
# reve =arr[::-1]
# print(reve)
# ==================
# nums = [2,7,11,15]
# target =9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])
    

# num=10
# num1=num
# rev =0
# while num >0:
#     rev =num%10 + rev*10
#     num =num//10
# print(rev)
# print(num1)
# if  rev ==num1 :
#     print("palindrome")
# else:    print("not palindrome")


# def roman_to_int(s):
#     value={
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000  
#     }
#     total=0
#     for i in range(len(s)-1):
#         if value(s[i])< value(s[i+1]):
#             total =total - value(s[i])
#         else:
#             total =total + value(s[i])
#     return total + value(s[-1])
    

# num = "123465"
# for i in range(len(num)):
#     print(num[i])


# m=int(input())
# n=int(input())
# mn=m+n
# num1=list(int(x) for x in input().split(","))
# num2 =list(int(x) for x in input().split(","))
# if len(num1) != m or len(num2) != n:
#     print("invalid input")
#     exit()

# merged=num1+num2
# merged.sort()
# if len(merged) != mn:
#     print("invalid input")
#     exit()
# print(merged)

# for i in range(5):
#     for j in range():
#         print("w",end =' ')
#     print()

def skipper(n):
    temp=n[0]
    print(temp)
    for i in range(0,len(n)-1):
        n[i]=n[i+1]
    n[-1]=temp
    print(temp)
    return n

#----------------------
#skip by k elements
# array=[5,1,1,2]
# even=0
# odd=0
# for i in array:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# if even==odd:
#     print("lead number")
# else:    print("not lead number")

# def skip_k(p):
#     k=3
#     k=k%len(p)
#     for i in range(k):
#         temp= p[-1] # last
#         for j in range(len(p)-1,0,-1):
#             p[j]=p[j-1]
#         p[0]=temp
#     return p


#-------------------------------
#bubble sortting
# array=[3,1,2,5]
# count = 0
# for i in  range(len(array)-1):
#     for j in range(len(array)-1-i):
#         count+=1
#         if array[j]>array[j+1]:
#             temp = array[j]
#             array[j]=array[j+1]
#             array[j+1]=temp
# print(array)
# print(count)
# print(len(array))




# num=[2,7,11,15]
# target = 9

# i=0
# j=len(num)-1
# print(num[j])
# while i<j :
#     sum1=num[i]+ num[j]
#     if sum1 == target:
#         print( num[i+1])
#         break
#     elif sum1 > target:
#         j-=1
#     else:
#         i+=1



# 26. Remove Duplicates from Sorted Array

num = [0,0,1,1,1,2,2,3,3,4]

k=1
for i in range(1,len(num)):
    if num[k-1] != num[i]:
        num[k]= num[i]
        k+=1
print(k)
      