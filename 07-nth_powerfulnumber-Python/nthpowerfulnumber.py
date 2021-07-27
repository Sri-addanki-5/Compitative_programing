# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


import math
def isPowerful(n):
    while (n % 2 == 0):
        a = 0
        while (n % 2 == 0):
            n = n // 2
            a = a + 1
        if ( a == 1):
            return False
    for power in range(3, int(math.sqrt(n))+1, 2):
        a = 0
        while (n % power == 0):
            n = n // power
            a = a + 1
        if (a == 1):
            return False
    return (n == 1)

def nthpowerfulnumber(n):
    x = 0
    y = 0
    while (x <= n):
        y += 1
        if(isPowerful(y)):
           x += 1
    return y


# Sum = 0
# Temp = n
# while(Temp > 0):
#     Reminder = Temp % 10
#     Factorial = math.factorial(Reminder)

#     print("Factorial of %d = %d" %(Reminder, Factorial))
#     Sum = Sum + Factorial
#     Temp = Temp // 10
# return n, sum
# # print("\n Sum of Factorials of a Given Number %d = %d" %(n, Sum))
    
# # if (Sum == n):
# #     print(" %d is a Strong Number" %n)
# # else:
# #     print(" %d is not a Strong Number" %Number)

# import math
# def nthpowerfulnumber(n):
#     # Your code goes here