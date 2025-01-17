# 21. Write a program to print the series : 10@9,9@8,8@7.......-5@-6

for i in range(10,-6,-1):
    print(i,"@",i-1,end="")
    if(i != -5):
        print(",",end="")
