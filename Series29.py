# 29. Write programs to print the following series. 0.5^2, 0.7^2,0.9^2....5.1^2
from decimal import Decimal, ROUND_HALF_UP
start =0.5
end=5.1
inc=0.2
current = start

while(current<=end):
    print(current,"^2",end="")
    current=Decimal(current)+inc