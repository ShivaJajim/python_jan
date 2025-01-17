# 20. Write a program to print A, B alternatively for 100 times. Ex: (A, B, A, B,
# A,B...)

for i in range(1,101):
    print("A,B", end =" ")
    if(i !=100):
        print(",",end="")