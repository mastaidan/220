from graphics import *


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        x = (shape.getP1().getX() + shape.getP2().getX()) / 2
        y = (shape.getP1().getY() + shape.getP2().getY()) / 2
        self.text = Text(Point(x, y), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, text):
        self.text.setText(text)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX() or self.shape.getP1().getX() >= point.getX() >= self.shape.getP2().getX():
            if self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY() or self.shape.getP1().getY() >= point.getY() >= self.shape.getP2().getY():
                return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)
