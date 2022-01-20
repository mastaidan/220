"""
Aidan Mast
Lab1.py
Calculate monthly interest based by asking inputs and running the numbers.
I certify that this assignment is entirely my own work.
"""


def monthly_interest():
    monthly_percent_int = eval(input("What is the annual interest?")) / 1200
    billing_cycle_length = eval(input("How long is billing cycle?"))
    net_balance = eval(input("What is the net balance?"))
    payment = eval(input("What was your payment?"))
    billing_day = eval(input("What day of the month did you pay on?"))
    step_1 = net_balance * billing_cycle_length
    step_2 = payment * (billing_cycle_length - billing_day)
    average_daily_balance = (step_1 - step_2) / billing_cycle_length
    monthly_interest = average_daily_balance * monthly_percent_int
    print("Your monthly interest is", monthly_interest, "!")
    print("If you would like to calculate another monthly interest, then type <monthly_interest()>.")

monthly_interest()`