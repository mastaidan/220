"""
Name: Aidan Mast
lab6.py

Problem: Encode a message using Vigenere cipher.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

# creates interface
win = GraphWin("Vigenere", 600, 400)
win.setCoords(0, 0, 10, 10)
message_entry = Entry(Point(6.5, 8), 30)
key_entry = Entry(Point(5, 6.5), 10)
box = Rectangle(Point(4, 5), Point(6, 4))
encode_button = Text(Point(5, 4.5), "Encode")
inst1 = Text(Point(3, 8), "Message to code")
inst2 = Text(Point(3, 6.5), "Enter Keyword")
message_entry.draw(win)
key_entry.draw(win)
box.draw(win)
encode_button.draw(win)
inst1.draw(win)
inst2.draw(win)
win.getMouse()
# gets and formats message and key; defines alphabet (i know the linting is wrong)
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
normal_message = message_entry.getText().upper().split(" ")
normal_message = "".join(normal_message)
normal_key = key_entry.getText().upper().split(" ")
normal_key = "".join(normal_key)
# converts message and key to numbers
message_length = len(normal_message)
number_message = []
number_key = []
for i in range(message_length):
    letter = normal_message[i]
    number = alphabet.index(letter)
    number_message.append(number)
key_length = len(normal_key)
for i in range(key_length):
    letter = normal_key[i]
    number = alphabet.index(letter)
    number_key.append(number)
# codes message as number
coded_number_message = []
for i in range(message_length):
    repeat_key_values = i % key_length
    coded_number = number_message[i] + number_key[repeat_key_values]
    coded_number_message.append(coded_number)
# converts code to letters
coded_message = []
for i in range(message_length):
    number = coded_number_message[i] % 26
    letter = alphabet[number]
    coded_message.append(letter)
coded_message = "".join(coded_message)
# updates interface
close_message = Text(Point(5, 2), "Click Anywhere to Close Window")
result_message = Text(Point(5, 4.5), "Resulting Message")
final_message = Text(Point(5, 4), coded_message)
encode_button.undraw()
box.undraw()
close_message.draw(win)
result_message.draw(win)
final_message.draw(win)
# pauses for click before closing window
win.getMouse()
win.close()