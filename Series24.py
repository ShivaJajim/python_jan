# 24. Write programs to print the following series. 5,10,5,10,5,10,5 for 7 times

for i in range(1,8):
    if(i%2==1):
        print("5",end="")
    else:
        print("10",end="")
    if(i !=7):
        print(",",end="")