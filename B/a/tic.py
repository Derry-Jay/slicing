"""
Created on Dec 12, 2018

@author: Vedha
"""


class Tic:
    def __init__(self):
        self.x = None

    def get(self):
        self.x = 123
        print(self.x ** 2)
