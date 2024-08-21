"""
Created on Dec 19, 2018

@author: Vedha
"""
# from math import ceil


l = int(input('Enter Limit:'))
for j in range(2, l):
    if isPrime(j):
        print(j)
