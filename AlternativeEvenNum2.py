# 14. Write a program to print alternate even numbers from 20 to 140. Like
# (22,26,30...)
# 22
# 26
# 30
# 34
# 38
# 42
# 46
# 50

count=0
for i in range(20,141):
    if(i%2==0):
        count=count+1
        if(count%2==0):
            print(i,end=" ")