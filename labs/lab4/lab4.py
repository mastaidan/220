"""
Name: Aidan Mast
lab4.py

Problem: Create a window that displays a Valentine's Card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import graphics
import time

win = graphics.GraphWin("(in russian accent) Have Good Valentine Day Yes", 700, 700)
win.setCoords(0, 0, 10, 10)
# creates window

circle1 = graphics.Circle(graphics.Point(3, 7), 2.25)
circle1.setOutline("red")
circle1.setFill("red")
circle2 = circle1.clone()
circle2.move(4, 0)
point1 = graphics.Point(.75, 7)
point1.move(.659, -1.5909)
point2 = graphics.Point(9.25, 7)
point2.move(-.659, -1.5909)
point3 = graphics.Point(5, 1)
based = graphics.Polygon(point1, point2, point3)
based.setOutline("red")
based.setFill("red")
filler = graphics.Circle(graphics.Point(5, 5), 2)
filler.setFill("red")
filler.setOutline("red")
circle1.draw(win)
circle2.draw(win)
based.draw(win)
filler.draw(win)
#creates heart

greeting = graphics.Text(graphics.Point(5, .75), "Happy Valentine's Day! Click to Shoot!")
greeting.setStyle("bold")
greeting.draw(win)
#create greeting

win.getMouse()
#pauses window for input

stem = graphics.Line(graphics.Point(0, 0), graphics.Point(1, 1))
end1 = graphics.Line(graphics.Point(0, 0), graphics.Point(-.4, 0))
end2 = graphics.Line(graphics.Point(0, 0), graphics.Point(0, -.4))
stem.setArrow("last")
stem.draw(win)
end1.draw(win)
end2.draw(win)
#creates arrow

for i in range(4):
    stem.move(1, 1)
    end1.move(1, 1)
    end2.move(1, 1)
    time.sleep(.1)
#moves arrow

end1.move(1, 1)
end2.move(1, 1)
stem.undraw()
stem = graphics.Line(graphics.Point(5, 5), graphics.Point(5.5, 5.5))
stem.draw(win)
#embeds arrow

greeting.setText("Click anywhere to close")

win.getMouse()
win.close()
#pauses window for input

