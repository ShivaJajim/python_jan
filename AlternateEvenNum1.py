# 13. Write a program to print alternate even numbers from 20 to 140. Like
# (20,24,28...)
# 20
# 24
# 28
# 32
# 36
# 40

num=20
num=140
count=0
for i in range(20,141):
    if(i%2==0):
        count=count+1
        if (count % 2 == 1):
            print(i,end=" ")




