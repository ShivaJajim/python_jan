# 1)Check for Even AND Positive Number:
# Write a Scala function to check if a given number is both even and positive.
# Sample Data:
# Number: 14

print("1)Check for Even AND Positive Number:")
a = 14
print("Given Number is:", a)
if(a%2 ==0):
    print("Even Number")
else:
    print("Not a Even number ")
# 2)Range Check with OR:
# Create a Scala program to determine if a given value is either less than -10 or greater than 10.
# Sample Data:
# Value: -15
print("2)Range Check with OR:")
a = -15
print("Given NUmber is :" , a)
if(a < -10 or 10 >a):
    print("given value is either less than -10 or greater than 10")
else:
    print("Nor a less than -10 or greater than 10")

# 3)Odd Number Check with AND:
# Implement a Scala function to check if a given number is odd and not divisible by 3.
# Sample Data:
# Number: 27
print("3)Odd Number Check with AND:")
a = 27
print("Given number is:",a)
if(a%2==1 and a%3 !=0):
    print("given number is odd and not divisible by 3")
else :
    print("given number is not odd and not divisible by 3.")

# 4)Divisibility by 4 OR 6:
# Write a Scala program to check if a given number is divisible by either 4 or 6.
# Sample Data:
# Number: 18

print("4)Divisibility by 4 OR 6")
a =18
print("Given Number is :", a)
if(a%4==0 or a%6 ==0):
    print("given number is divisible by either 4 or 6")
else:
    print("given number is not divisible by either 4 or 6")

# 5)Eligibility for Voting OR Driving:
# Create a Scala program to check if a person is eligible to vote (age greater than or equal to 18) or
# eligible to drive (age greater than or equal to 16).
# Sample Data:
# Age: 20

print(" 5)Eligibility for Voting OR Driving:")
a =20
print("GIven number is :",a)
if(a >=18 or a >=16):
    print("person is eligible to vote (age greater than or equal to 18) or\
     eligible to drive (age greater than or equal to 16).")
else:
    print("Not eligible")

# 6)Multiple Range Check:
# Write a Scala function to check if a given number is in the range [1, 10] or [20, 30].
# Sample Data:
# Number: 25

print(" 6)Multiple Range Check:")
a =25
print("GIven number is:" , a)
if((a >= 1 and a<=10) or (a>=20 and a<= 30)):
    print("given number is in the range [1, 10] or [20, 30]")
else:
    print("given number isnot in the range [1, 10] or [20, 30]")

# 7)Check for Negative AND Odd Number:
# Implement a Scala program to check if a given number is both negative and odd.
# Sample Data:
# Number: -7

print("7)Check for Negative AND Odd Number:")
a =-7
print("Given number is :",a)
if(a<0 and a%2 ==1):
    print("given number is both negative and odd")
else:
    print("given number is not both negative and odd")

# 8)Eligibility for Senior Discount OR Student Discount:
# Create a Scala program to check if a person is eligible for a senior citizen discount (age greater than
# 60) or a student discount (age less than 25).
# Sample Data:
# Age: 63

print("8)Eligibility for Senior Discount OR Student Discount:")
a=63
print("Given number is :",a)
if(a>60 or a<25):
    print("person is eligible for a senior citizen discount (age greater than\
 60) or a student discount (age less than 25).")
else:
    print("Not eligible ")

# 9)Divisibility by 5 AND 7:
# Write a Scala function to check if a given number is divisible by both 5 and 7.
# Sample Data:
# Number: 35

print("9)Divisibility by 5 AND 7:")
a =35
print("Given number is :",a)
if(a%5==0 and a%7==0):
    print("given number is divisible by both 5 and 7")
else:
    print("given number is not divisible by both 5 and 7")


# 10)Check for Non-Negative OR Even Number:
# Create a Scala program to check if a given number is either non-negative or even.
# Sample Data:
# Number: -8
print("10)Check for Non-Negative OR Even Number:")
a =- 8
print("Given number is :",a)
if(a>0 or a%2 ==0):
    print("given number is either non-negative or even.")
else:
    print("given number is not either non-negative or even.")

# 11)Check for Prime AND Odd Number:
# Write a Scala function to check if a given number is both a prime number and an odd number.
# Sample Data:
# Number: 17

print("11)Check for Prime AND Odd Number:")
a=17
count=0
print("Given number is :" ,a)
for i in range(1,18):
    if(a%i ==0):
        count=count+1

if(count==2):
    print("Given number is prime")
else :
    print("NOt a prime ")

# 12)Eligibility for Discount OR Free Shipping:
# Create a Scala program to check if a customer is eligible for a discount (purchase amount greater
# than 150) or qualifies for free shipping (purchase amount greater than 100).
# Sample Data:
# Purchase Amount: 120
print("12)Eligibility for Discount OR Free Shipping:")
a =120
print("GIven number is :",a)
if(a>150 or a>100):
    print("customer is eligible for a discount (purchase amount greater\
 than 150) or qualifies for free shipping (purchase amount greater than 100).")
else:
    print("Not eligible")

# 13)Divisibility by 3 OR 8:
# Write a Scala function to check if a given number is divisible by either 3 or 8.
# Sample Data:
# Number: 24
print("13)Divisibility by 3 OR 8:")
a =24
print("Given number is :",a)
if(a%3 or a%8):
    print("given number is divisible by either 3 or 8")
else:
    print("given number is not divisible by either 3 or 8")

# 14)Check for Non-Positive AND Even Number:
# Implement a Scala program to check if a given number is both non-positive and even.
# Sample Data:
# Number: -6
print("14)Check for Non-Positive AND Even Number:")
a=-6
print("given number is :",a)
if(a<=0 and a%2==0 ):
    print("given number is both non-positive and even")
else:
    print("given number is not both non-positive and even")

# 15)Age Group Classification with AND:
# Create a Scala program to classify a person&#39;s age group. Classify them as a child (less than 13),
# teenager (between 13 and 19), and an adult (20 and above) using both logical AND and OR.
# Sample Data:
# Age: 15
print("15)Age Group Classification with AND")
a = 15
print("Given number is",a)
if(a<13):
    print("Child")
elif(a>= 13 and a<=19):
    print("Teenager")
elif(a>=20):
    print("adult")
else:
    print("Invalide age")

# 16)Check for Divisibility by 2 OR 5:
# Write a Scala function to check if a given number is divisible by either 2 or 5.
# Sample Data:
# Number: 25
print("16)Check for Divisibility by 2 OR 5:")
a=25
print("Given number is :",a)
if(a%2==0 or a %5==0):
    print("given number is divisible by either 2 or 5")
else:
    print("given number is not divisible by either 2 or 5")

# 17)Eligibility for Senior Discount AND Student Discount:
# Create a Scala program to check if a person is eligible for both a senior citizen discount (age greater
# than 60) and a student discount (age less than 25).
# Sample Data:
# Age: 70
print("17)Eligibility for Senior Discount AND Student Discount")
a =70
print("Given number is ",a)
if(a>60 and a<25):
    print("person is eligible for both a senior citizen discount (age greater\
# than 60) and a student discount (age less than 25)")
else:
    print("Not eligible")

# 19)Check for Multiple of 3 AND 7:
# Implement a Scala function to check if a given number is both a multiple of 3 and 7.
# Sample Data:
# Number: 21
print("19)Check for Multiple of 3 AND 7:")
a =21
print("Given Number is:",a)
if(a%3==0 and a%7==0):
    print("given number is both a multiple of 3 and 7.")
else :
    print("given number is not both a multiple of 3 and 7.")

# 20)Divisibility by 5 OR 9:
# Write a Scala program to check if a given number is divisible by either 5 or 9.
#
# Sample Data:
# Number: 45

print("20)Divisibility by 5 OR 9")
a=45
print("Given number is :",a)
if(a%5 ==0 or a%9==0):
    print("given number is divisible by either 5 or 9")
else:
    print("given number is not divisible by either 5 or 9")

# 21)Check for Odd AND Not Divisible by 4:
# Create a Scala program to check if a given number is both odd and not divisible by 4.
# Sample Data:
# Number: 15

print("21)Check for Odd AND Not Divisible by 4:")
a= 15
print("Given number is:",a)
if(a%2==1 and a%4 !=0):
    print("given number is both odd and not divisible by 4")
else:
     print("given number is not both odd and not divisible by 4")

# 23)Eligibility for Discount OR Membership Benefits:
# Create a Scala program to check if a customer is eligible for a discount (purchase amount greater
# than 200) or qualifies for membership benefits (loyalty card available).
# Sample Data:
# Purchase Amount: 180
# Loyalty Card: true

print("23)Eligibility for Discount OR Membership Benefits:")
a=180
card=True
print("Given amount and curda are :",a,card)
if(a>200 or card ==True):
    print("customer is eligible for a discount (purchase amount greater\
# than 200) or qualifies for membership benefits (loyalty card available)")
else:
    print("Not eligible")

# 24)Divisibility by 2 OR 3:
# Write a Scala function to check if a given number is divisible by either 2 or 3.
# Sample Data:
# Number: 9

print("24)Divisibility by 2 OR 3")
a=9
print("given number is:",a)
if(a%2==0 or a%3==0):
    print("given number is divisible by either 2 or 3")
else:
    print("given number is not divisible by either 2 or 3")

# 25)Check for Positive AND Not Divisible by 3:
# Implement a Scala program to check if a given number is positive and not divisible by 3.
# Sample Data:
# Number: 7

print("25)Check for Positive AND Not Divisible by 3")
a =7
print("GIven number is :",a)
if(a>0 and a%3==0):
    print("given number is positive and not divisible by 3")
else:
    print("given number is not  positive and not divisible by 3")

# 26)Eligibility for Senior Discount AND Not a New Customer:
# Create a Scala program to check if a person is eligible for a senior citizen discount (age greater than
# 65) and is not a new customer.
# Sample Data:
# Age: 70
# New Customer: false

print("26)Eligibility for Senior Discount AND Not a New Customer")
a=70
customer =False
if(a>60 and customer==False):
    print("person is eligible for a senior citizen discount (age greater than\
# 65) and is not a new customer.")
else:
    print("NOt eligible")

# 27)Check for Odd OR Prime Number:
# Write a Scala function to check if a given number is either odd or a prime number.
# Sample Data:
# Number: 11
print("27)Check for Odd OR Prime Number")
a =11
print("given number is :",a)
if(a%2==1):
    print("given number is odd")
    count=0
    for i in range(1,a+1):
        if(a%i==0):
            count=count+1

    if(count==2):
        print("GIven number is ODD and prime ")
    else:
        print("NOt a prime ")

# 28)Eligibility for Discount AND Free Shipping:
# Create a Scala program to check if a customer is eligible for a discount (purchase amount greater
# than 150) and qualifies for free shipping (purchase amount greater than 100).
# Sample Data:Purchase Amount: 120
print("28)Eligibility for Discount AND Free Shipping:")
a=120
print("Given Number is :",a)
if(a>150 and a >100):
    print("a customer is eligible for a discount (purchase amount greater\
# than 150) and qualifies for free shipping (purchase amount greater than 100).")
else:
    print("not a eligible")

# 29)Check for Non-Negative AND Not Divisible by 7:
# Implement a Scala program to check if a given number is non-negative and not divisible by 7.
# Sample Data:
# Number: 14
print("29)Check for Non-Negative AND Not Divisible by 7")
a=14
print("Given number is :",a)
if(a>=0 and a%7==0):
    print("given number is non-negative and not divisible by 7")
else:
    print("given number is not non-negative and not divisible by 7")

# 30)Eligibility for Student Discount OR Free Trial:
# Write a Scala program to check if a person is eligible for a student discount (age less than 25) or is
# eligible for a free trial.
# Sample Data:
# Age: 22
# Free Trial: true
print("30)Eligibility for Student Discount OR Free Trial")
a=22
Trial=True
if(a<25 or Trial== True):
    print("person is eligible for a student discount (age less than 25) or is\
# eligible for a free trial.")
else:
    print("Not a eligible")

# 31)Check for Divisibility by 4 OR 6:
# Create a Scala function to check if a given number is divisible by either 4 or 6.
# Sample Data:
# Number: 24
print("31)Check for Divisibility by 4 OR 6:")
a=31
print("Given number is",a)
if(a%4 ==0 or a%6==0):
    print("given number is divisible by either 4 or 6")
else:
    print("given number is not divisible by either 4 or 6")




