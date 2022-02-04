"""
Name: Aidan Mast
lab3.py

Problem: Calculate three different averages using math and loops.4

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
roads = eval(input("How many roads were surveyed?"))
grand_total = 0
for i in range(roads):
    print("How many days was road", i + 1, "surveyed?", end="")
    days = eval(input())
    total = 0
    for j in range(days):
        print("How many cars traveled on day", i + 1, "?", end="")
        cars = eval(input())
        total = cars + total
    grand_total = grand_total + total
    print("Road", i + 1, "average vehicles per day:", round(total / days, 2))
print("Total number of vehicles traveled on all roads:", grand_total)
print("Average number of vehicles per road:", round(grand_total / roads, 2))
