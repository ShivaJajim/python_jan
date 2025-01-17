# 1)Print numbers from 1 to 5 using a for loop.
print("1)Print numbers from 1 to 5 using a for loop")
for i in range(1,6):
    print(i)

# 2)Print even numbers from 2 to 10 using a while loop.
print("2)Print even numbers from 2 to 10 using a while loop.")

a=2
while(a<=10):
    print(a)
    a=a+1
# 3)Calculate the sum of all numbers from 1 to 50 using a for loop.
print("3)Calculate the sum of all numbers from 1 to 50 using a for loop.")
sum=0
for i in range(1,50):
    sum=sum+i
print("Sum of 50 Numbers is: " , sum)

# 4)Print the square of numbers from 1 to 5 using a for loop.
print("4)Print the square of numbers from 1 to 5 using a for loop.")
for i in range(1,6):
    print(i,"Square is :",i*i)

# 5)Print the reverse of a given list using a while loop.
print("5)Print the reverse of a given list using a while loop.")
a =[12,13,45,667]
print(len(a),a[1],a[0])
b =[0]*len(a)
# for i in range(4,0,-1):
#     b[4-i]=a[i]
# for i in range(0,len(b)):
#     print(b[i])

# 6)Generate and print the first 5 multiples of 3 using a for loop.
print("# 6)Generate and print the first 5 multiples of 3 using a for loop.")
for i in range(1,6):
    print(i*3)

# 7)Print odd numbers from 1 to 15 using a while loop.
print("7)Print odd numbers from 1 to 15 using a while loop.")
for i in range ( 1,16):
    if(i%2--1):
        print(i)

# 8)Calculate the factorial of a given number using a for loop.
print("8)Calculate the factorial of a given number using a for loop.")
fact=1
for i in range(1,6):
    fact=fact*i

print(fact)

# 9)Print the characters of a string in reverse order using a for loop.
print("9)Print the characters of a string in reverse order using a for loop.")
str='shiva'
l=len(str)
print(l)
str2=""
for i in range(l-1,-1,-1):
    # print(i)
    str2=str2+str[i]

print(str2)

# 10)Check if a number is prime using a while loop.
print("10)Check if a number is prime using a while loop.")
num=11
count=0
i=1
while(i<=num):
    if(num%i==0):
        count=count+1
    i=i+1

if(count==2):
    print("Given number is prime")
else:
    print("not a prime")

# 11)Print the elements of a list in reverse order using a for loop.
print("11)Print the elements of a list in reverse order using a for loop.")
myarry=[12.4,65,7]
print(len(myarry))
myarry2=[0]*len(myarry)

# for i in range( len(myarry),-1,-1):
#     myarry2[len(myarry)-i]=myarry[i]
#
# for i in range(0,myarry2):
#     print(myarry2[i])

# 12)Find the sum of all even numbers from 1 to 20 using a while loop.
print("12)Find the sum of all even numbers from 1 to 20 using a while loop.")
sum=0
for i in range(1,21):
    if(i%2 == 0):
        sum=sum+1

print(sum)

# 13)Check if a string is a palindrome using a for loop.
print("13)Check if a string is a palindrome using a for loop.")

num=121
temp = num
res3=0
while(num != 0):
    s=num%10

    res3=(res3*10)+s
    num=num//10

if(temp==res3):
    print("palindrome")

# 14)Print the cube of numbers from 1 to 3 using a while loop.

print("# 14)Print the cube of numbers from 1 to 3 using a while loop.")

for i in range(1,4):
    print(i,"cube of :",i*i*i)

# 15)Count the number of vowels in a given string using a for loop.
print("# 15)Count the number of vowels in a given string using a for loop.")
str ="shiva"
print(len(str))
str2='aeiou'
count=0

for i in range(0,len(str)):

    for j in range(0,len(str2)):
        if(str[i] == str2[j]):
            count=count+1

print(count)

# 16)Print the elements of a list using a while loop.
print("16)Print the elements of a list using a while loop.")
a=[12,13,14,5]
i=0
while(i<=len(a)-1):
    print(a[i])
    i=i+1

# 17)Calculate the product of numbers from 1 to 5 using a for loop.
print("17)Calculate the product of numbers from 1 to 5 using a for loop.")
prd=1
for i in range(1,6):
    prd=prd*i
print(prd)

# 18)Check if a given number is a perfect square using a while loop.
print("18)Check if a given number is a perfect square using a while loop.")
num = 5
sq=0
count=0
for i in range(1,16):
    sq=i*i
    if(sq == num):
        count=count+1

if(count==1):
    print("GIven number is perfect number ")
else:
    print("Not a perfect number ")


