#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")


# In[2]:


num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "it is a COMPOSITE number")


# In[3]:


def isPalindrome(string):
    if string==string[::-1]:
        return "it is a palindrome"
    else:
        return "it is not a palindrome"

s1="MALAYALAM"
s2="dgahaafr"
print(s1,":",isPalindrome(s1))
print(s2,":",isPalindrome(s2))


# In[4]:


string = "aefsdfggrhfghfghngjuyhgggfgnbghjngfjhgjg"
result = {}

for i in string:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print("Result is:- ", result)


# In[ ]:




