"""
Name: Aidan Mast
lab2.py

Problem: Calculate three different averages using math and loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def mean():
    values = eval(input("enter the values to be entered:"))
    rms_total = 0
    har_total = 0
    geo_total = 1
    for i in range(values):
        l = eval(input("enter value"))
        rms_total = rms_total + l ** 2
        har_total = har_total + (1 / l)
        geo_total = geo_total * l
    rms_mean = math.sqrt(rms_total / values)
    har_mean = values / har_total
    geo_mean = geo_total ** (1 / values)
    print(round(rms_mean, 3))
    print(round(har_mean, 3))
    print(round(geo_mean, 3))
