"""
Name: Aidan Mast
lab13.py

Problem: Practice sorting algorithms and make a capstone.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    text = open(filename, 'r')
    text = text.readline().split(" ")
    for index in range(len(text)):
        if int(text[index]) > 830:
            print("WARNING!!! HIGH TRADE VOLUME. Timestamp {} second(s).".format(index))
        if int(text[index]) == 500:
            print('ALERT! 500 Trade Volume Reached. Timestamp {} second(s)'.format(index))



def main():
    trade_alert('trades.txt')


main()
