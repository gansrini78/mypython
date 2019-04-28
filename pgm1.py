# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 02:08:37 2017

@author: Ganesh Srinivasan
"""

def milestokm(mile):
    km=mile*1.6
    print(km,"km")
    
# input through an interactive input
m=input("pls enter miles: ")
m=float(m) # since there text entered in input,
#python thinks that m is a string ,so convert to float to avoid error
milestokm(m)