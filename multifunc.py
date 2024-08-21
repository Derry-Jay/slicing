"""
Created on Nov 30, 2018
@author: Vedha
"""
from pip._vendor.distlib.compat import raw_input

nm = raw_input('')
age = int(input("enter the age"))
if age >= 18:
    print("eligible")
else:
    print("not eligible")
