#1 string reverce
'''n = input()
print(n[::-1])'''

#count the vowel or constant
'''
n =input()
count=0
rev = 0
for i in range(0,len(n)):
    ch  = n[i].lower()
    if ch in "aeiou":
        count+=1
        
    elif ch.isalpha():
        rev+=1
        
print("vowel:",count)
print("constant:",rev)
'''

#check palindrome 
'''
n = input()
m = n[::-1]
if n == m:
    print("palindrome")
else:
    print("Not palindrome")'''

"""#Frequencey of each character

n = input()
done = set()
for i in n:
    if i ==" ":
        continue
    if i not in  done :
        print(i,":",n.count(i))
        done.add(i)
"""
# method 2
n = input()
result = {}

for i in n:
    if i ==" ":
        continue
    if i in result:
        result[i] +=1
    else:
        result[i]=1
for i,j in result.items():
    print(i,":",j)

#remove space from string
'''    
n = input()
result = n.replace(" ","")
print(result)'''

#method 2
'''
n = input()
result=""
for i in n:
    if i != " ":
        result +=i
print(result)
'''    