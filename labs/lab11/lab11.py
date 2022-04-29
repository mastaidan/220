"""
Name: Aidan Mast
lab11.py

Problem: Create a three door game where the user guesses a door.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from lab10.button import Button
from lab10.door import Door
from random import randint
from graphics import *
from lab10.button import Button
from lab10.door import Door


def win_round(win_count, top_text, bottom_text, win_box):
    win_count += 1
    top_text.setText("You win!")
    bottom_text.setText("Click anywhere to play again")
    win_box.set_label(win_count)


def lose_round(lose_count, top_text, bottom_text, lose_box):
    lose_count += 1
    top_text.setText("L")
    bottom_text.setText("Click anywhere to play again")
    lose_box.set_label(lose_count)


win_count = 0
lose_count = 0


def main():
    # creates window
    win = GraphWin("Three Door Game", 500, 500)
    win.setCoords(0, 0, 10, 10)

    # creates doors
    door1 = Door(Rectangle(Point(1, 1.5), Point(3, 6.5)), "Door 1")
    door2 = Door(Rectangle(Point(4, 1.5), Point(6, 6.5)), "Door 2")
    door3 = Door(Rectangle(Point(7, 1.5), Point(9, 6.5)), "Door 3")
    door1.color_door("grey")
    door2.color_door("grey")
    door3.color_door("grey")
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)

    # creates button and text
    button = Button(Rectangle(Point(7, 8), Point(9, 9.5)), "Quit")
    bottom_text = Text(Point(5, .5), "Click to guess the secret door")
    top_text = Text(Point(5, 7), "I have a secret door")
    button.draw(win)
    bottom_text.draw(win)
    top_text.draw(win)

    # creates scoreboard
    win_box = Button(Rectangle(Point(1, 8), Point(2, 9)), 0)
    lose_box = Button(Rectangle(Point(2, 8), Point(3, 9)), 0)
    win_text = Text(Point(1.5, 9.5), "Win")
    lose_text = Text(Point(2.5, 9.5), "Lose")
    win_box.draw(win)
    lose_box.draw(win)
    win_text.draw(win)
    lose_text.draw(win)

    # controls door and button
    game = 1
    while game:
        x = 1
        while x:
            click = win.getMouse()
            rand_value = randint(1, 3)
            if rand_value == 1:
                door1.set_secret(True)
            elif rand_value == 2:
                door2.set_secret(True)
            elif rand_value == 3:
                door3.set_secret(True)
            if door1.is_clicked(click):
                if door1.is_secret():
                    door1.open("green", "Door 1")
                    win_round(win_count, top_text, bottom_text, win_box)
                else:
                    door1.close("red", "Door 1")
                    lose_round(lose_count, top_text, bottom_text, lose_box)
            elif door2.is_clicked(click):
                if door2.is_secret():
                    door2.open("green", "Door 2")
                    win_round(win_count, top_text, bottom_text, win_box)
                else:
                    door2.close("red", "Door 2")
                    lose_round(lose_count, top_text, bottom_text, lose_box)
            elif door3.is_clicked(click):
                if door3.is_secret():
                    door3.open("green", "Door 3")
                    win_round(win_count, top_text, bottom_text, win_box)
                else:
                    door3.close("red", "Door 3")
                    lose_round(lose_count, top_text, bottom_text, lose_box)
            if button.is_clicked(click):
                win.close()
                return
            x = 0
        if button.is_clicked(win.getMouse()):
            win.close()
            return
        door1.set_secret(False)
        door2.set_secret(False)
        door3.set_secret(False)
        door1.color_door("grey")
        door2.color_door("grey")
        door3.color_door("grey")
        bottom_text.setText("Click to guess the secret door")
        top_text.setText("I have a secret door")

        if button.is_clicked(win.getMouse()):
            win.close()
            return

    win.getMouse()


main()
