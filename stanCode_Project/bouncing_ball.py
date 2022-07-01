"""
File: 
Name: Lina Chou
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
times = 0
vy = 0
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    window.add(ball)
    onmouseclicked(move)


def move(mouse):
    """
    :param mouse: mouse event, stores mouse information
    """
    global times
    global vy
    if ball.y == START_Y:  # 當球的高度等於初始值
        if times < 3:  # 使球的彈跳次數不超過三次
            while True:
                ball.move(VX, vy)
                if ball.y >= window.height - SIZE:  # 當球超出底下視窗
                    if vy > 0:
                        vy = -vy  # 改變球的放向
                        vy *= REDUCE

                vy += GRAVITY
                if ball.x >= window.width:  # 當球超出右邊視窗,使球回到起始點
                    window.add(ball, x=START_X, y=START_Y)
                    times += 1
                    vy = 0
                    break
                pause(DELAY)


if __name__ == "__main__":
    main()
