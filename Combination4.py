# 4. Write a java program that performs the following tasks.
# a. Store a number in a variable
# b. If value is not in range (100-1000) prints wrong number else follows
# the steps
# c. Check even or odd
# d. If even divide the number by 3 and print the remainder
# e. If odd divide the number by 2 and print the remainder.

i =100

if(i>=100 and i<=1000):
    if(i%2==0):
        print("even number")
        re1=i%3
        print(re1)
    else:
        print("Odd ")
        re1=i%2
        print(re1)
else:
    print("Wrong NUmber")

