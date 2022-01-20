"""
Aidan Mast
Lab1.py
Calculate monthly interest based on asked inputs
I certify that this assignment is entirely my own work.
"""
def monthly_interest():
    monthly_percent_int = eval(input("gimme annual int please"))/1200
    billing_cycle_length = eval(input("how long is billing cycle please"))
    net_balance = eval(input("gimme net balance please"))
    payment = eval(input("gimme payment please"))
    billing_day = eval(input("gimme billing day please"))
    step_1 = net_balance * billing_cycle_length
    step_2 = payment * (billing_cycle_length - billing_day)
    average_daily_balance = (step_1 - step_2) / billing_cycle_length
    monthly_interest = average_daily_balance * monthly_percent_int
    print("your monthly interest is", monthly_interest,"!")

