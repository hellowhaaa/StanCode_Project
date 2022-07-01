"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The game, break out, aims to clear all bricks on the screen without ball falling off the frame.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    global NUM_LIVES
    while True:
        dx = graphics.get_velocity_x()  # 得到球x,y 的初始速度
        dy = graphics.get_velocity_y()
        graphics.ball.move(dx, dy)
        pause(FRAME_RATE)
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics.change_x()  # 當球碰壁時反彈, dx = -dx
        if graphics.ball.y <= 0:
            graphics.change_y()  # 當球碰壁時反彈, dy = -dy
        if graphics.ball.y >= graphics.window.height - graphics.ball.height:
            graphics.reset_ball()  # 當球的y值大於視窗,掉出視窗時, 重製球的位置,重新開始
            NUM_LIVES -= 1
            if NUM_LIVES == 0:  # 當命扣完時不再跑迴圈,不再使球移動
                break
        graphics.remove()  # 移除磚塊
        graphics.all_clear()  # 當所有磚塊被消除時


if __name__ == '__main__':
    main()
