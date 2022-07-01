"""
File: 
Name: Arya Chou
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow(800, 800)
start = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(circle)


def circle(mouse):
    start.x = mouse.x - SIZE / 2
    start.y = mouse.y - SIZE / 2
    start.filled = False
    start.color = 'black'
    window.add(start)
    onmouseclicked(line)


def line(mouse):
    window.remove(start)
    straight = GLine(start.x + SIZE/2, start.y + SIZE/2, mouse.x - SIZE/2, mouse.y - SIZE/2)
    straight.color = 'black'
    window.add(straight)
    onmouseclicked(circle)







if __name__ == "__main__":
    main()
