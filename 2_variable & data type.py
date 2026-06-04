#!
"""n = str("12345678")
m = int(n)
print(m)"""

#2 perform a arthimetic operation
 #with conditionals   
"""a,b = map(int,input().split())
op = input("+,-,*,/:")
if op== "+":
    print("result:",a+b)
elif op == "-":
    print("result:",a-b)
elif op == "*":
    print("result:",a*b)
elif op == "/":
    print("result:",a/b)

else:
    print("not valid")"""


#with functions
"""def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    return a/b
    
a,b = map(int,input().split())
op = input("+,-,*,/:")
if op== "+":
    print("result:",sum(a,b))
elif op == "-":
    print("result:",sub(a,b))
elif op == "*":
    print("result:",mul(a,b))
elif op == "/":
    print("result:",div(a,b))

else:
    print("not valid")"""

#complex
"""def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    if b==0:
        print("Division is not posibile")
        
    return a/b
    
a,b = map(int,input().split())
print("choice1:addition")
print("choice2:subtration")
print("choice3:multplecation")
print("choice4:division")
op=input("1,2,3,4:")
if op== "1":
    print("result:",sum(a,b))
elif op == "2":
    print("result:",sub(a,b))
elif op == "3":
    print("result:",mul(a,b))
elif op == "4":
    print("result:",div(a,b))

else:
    print("not valid")"""

#calculator multi inputs
"""def add(num):
    return sum(num)
def sub(num):
    result=num[0]
    for i in num[1:]:
        result=result-i
    return result
def mul(num):
    result=num[0]
    for i in num[1:]:
        result=result*i
    return result
def div(num):
    if num[1:]==0:
        print("non div")
    result=num[0]
    for i in num[1:]:
        result=result/i
    return result
def rem(num):
    result=num[0]
    for i in num[1:]:
        result=result%i
    return result
def que(num):
    result=num[0]
    for i in num[1:]:
        result=result//i
    return result
    
num = list(map(float,input("Enter a number:").split()))
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.rem")
print("6.que")

op = input("Enter number:")
if op=='1':
    print("result:",add(num))
elif op=='2':
    print("result:",sub(num))
elif op=='3':
    print("result:",mul(num))
elif op=='4':
    print("result:",div(num))
elif op=='5':
    print("result:",rem(num))
elif op=='6':
    print("result:",que(num))
else:
    print("none")"""


#int to binary
"""n = int(input())
binary = bin(n)
print(binary)"""


#4
"""print("1.F to C")
print("2.C to F")
n = int(input("Enter number convertion:"))
m = int(input())
if n == 1:
    cel = ((m-32)*5/9)#(m-32)*5/9
    print(cel,'C')
elif n==2:
    far= ((m*9/5)+32)
    print(far,'F')
else:
    print("none")"""

