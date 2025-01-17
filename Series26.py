# 26. Write programs to print the following series.
# 1,even,3,even,5,even,.......35,even

for i in range(1,36):
    print(i,",even",end="")
    if(i !=35):
        print(",",end="")