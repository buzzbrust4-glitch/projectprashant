# # print("hello")
# # #print("hello")

# # #sort
# # list=[2,5,1,4,8]

# # list.sort()
# # print(list)

# # list=[2,5,1,4,8,]

# # list.sort(reverse=True)
# # print(list)
# # print(text.upper)  #uotput:HELLO PYTHON
# # print(text.lower)  #outout:hello python
# # print(text.script)  #output:hello python 
# # print(text.replace("python","world"))#output: hello world
# # print(text.spilt()) #output(hello,'python')


# # x=5
# # y="block"

# # #format string

# # age=20
# # print(x+y)

# # name="bob"
# # y=20
# # print(f"my name is (x) and my age is {y}")











# # x=5
# # x+=3
# # x*
# # print(x)

# # print(x==y)
# # print(x|=y)
# # print(x>=y)
# # print(x<=y)
# # print(x>y)
# # print(x<y)




# # x=8
# # y=x

# # print(y)
# # print(z is y)
# # print(x is not y)


# # colors={"red","green","blue"}
# # for x in colors:
# #     print(X)



# #     students={
# #         "name":"chander",
# #     "age":30,
# #     "grades":"A"
# #     }
# #     print(student)








# #     #if else

# #     age=18

# #     if age>=18
# #     print("you are adult")
# #     else:
# #         print("you are not adult")



# #         x=15

# #         if x>10:
# #             print("x is greatet than 10")
            
# #             if x>20
# #                print("x is greater than 20")
# #             else:
# #                 print("x is not greater than 20")
                
            
# # x=15

# # ifx%2==0:
# #    print("even")
# # else:
# #     print("odd") 




# #     word="python"

# #     for x in word:
# #          print(x)  



# #loops 

# #words='"python"

# # for i in range(5):
#    # print(I)
# for i in range (1,10,2):
#     print(i) 

#     for i in range (1,4):
#         print(i)  


#         for i in range(1,4):
#             for j in range(1,3):
                
#                 print(f"i={i},j={j}")
#      for 10 in range(1,4):
#      for j in range(1,3):
#          print(f"i={i},j={j}")

#          for 10 in range(1,6):  
#            if==4:
#             break
#         print(1)           
#  for 1 in range (1,20):
#     print(i)

#     #quei 2nd

#     for even in range (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):
#         print(even)

#         for i in range (yellow,pink,white,black)
#         # print()

#         #function
#         def greet(name):
#             print(f"hello,{name}")

#         greet("alice")
#         greet("bob")

#         def add(a,b):
#             return a+b

#             result=add(5,3)
#             print(result)#8

#             def subtract(a,b):
#                 return a-b
#                 result=subtract(5,3)
#                 print(result) #2





# x=12

# def my_fun()

# print(x)
# print(y)








# #class
   
#         class car:
#             def_int_(self,brand,color)
#             self.brand=brand #Attribute
#             self.color= color #Attribute

#             def drive("self"): #method
#                 print(f"{self.color}{self.brand}is driving)
                
#                 #object
#                 car1=car("bmw","Black")
#                 car2=car("tesla","white")













# #Array

# import array

# number=array.array('i',[1,2,3,4,5])
# print(number)


# python -m pip install numpy




# from numpy import random

# x=random.randient(100)
# print(x)




# [54]
# [1,2,3,4,5]

# [[[1,2,3],
#  [4,5,6]]
#  [[7,8,9],
#  [10,11,12]]]
#from numpy import random

# x=random.randient(100)
# print(x)

#x=random.rand()
#print(x)

#  x=random.randit(100,size=(3,5))
#  print(x)


#  x=random.randit(100,size=(2,3,5))
#  print(x)


#   x=random.choice([4,5,6],size=(5))
#   print(x)


# x=random.choice([4,5,6],size=(2,3,5))
# print(x)
### python -m pip install pandas

###pandas

import pandas as pd 

data=[10,20,30,40]

s=pd.Series(data)

print(s)


import pandas as pd 

data={

  "Name":["Alice","Bob","Charlie","David"],

  "Age":[24,27,22,32],

  "City":["Delhi","Mumbai","Chennai","Kolkata"]
  }
  
df=pd.DataFrame(data)

print(df)

import numpy as np


arr=np.array([1,2,3,4,5])

s=pd.Series(arr)
print(s)


data={"Math":90,"Science":85,"English":78}

s=pd.Series(data)

print(s)