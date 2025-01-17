# 25. Write programs to print the following series. 5*4,5*3,5*2,......5*(-12)
# (Print in two ways – patter & multiplied value)

for i in range(4,-13,-1):
    print("5*",i,end="")
    if(i != -12):
        print(",",end="")