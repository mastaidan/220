from graphics import *


class Door:

    def __init__(self, shape, label):
        self.shape = shape
        x = (shape.getP1().getX() + shape.getP2().getX()) / 2
        y = (shape.getP1().getY() + shape.getP2().getY()) / 2
        self.text = Text(Point(x, y), label)
        self.secret = False

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

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def is_secret(self):
        if self.secret:
            return True
        return False

    def set_secret(self, secret):
        self.secret = secret

    def is_clicked(self, point):
        if self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX() or self.shape.getP1().getX() >= point.getX() >= self.shape.getP2().getX():
            if self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY() or self.shape.getP1().getY() >= point.getY() >= self.shape.getP2().getY():
                return True
        else:
            return False

    def color_door(self, color):
        self.shape.setFill(color)
