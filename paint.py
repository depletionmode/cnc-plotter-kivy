from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

def generateGCode(lines, width):
    # normalize
    scale = 400/width;
    print(scale)
    print(lines[-1].points)

class PaintCanvas(Widget):
    lines = []

    def on_touch_down(self, touch):
        with self.canvas:
            Color(255,0,0)
            if self.collide_point(touch.x, touch.y):
                self.lines.append(Line(points=(touch.x, touch.y), width=4))

    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.lines[-1].points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        print(len(self.lines))
        generateGCode(self.lines, self.width)


class MainWidget(Widget):
    pass


class MyPaintApp(App):

    def build(self):
        main = MainWidget();
        clearbtn = Button(text='Clear')
        printbtn = Button(text='Print')
        #clearbtn.bind(on_release=self.clear_canvas)
        #main.add_widget(clearbtn)
        #main.add_widget(printbtn)
        self.main = main
        return main

if __name__ == '__main__':
    MyPaintApp().run()
