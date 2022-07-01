"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

The game, break out, aims to clear all bricks on the screen without ball falling off the frame.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10      # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'

        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-PADDLE_OFFSET))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius, x=(self.window.width-ball_radius)/2,
                          y=(self.window.height-ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)

        # Draw bricks
        # 創造磚塊
        self.all_brick = 0
        for i in range(0, brick_rows):
            color = ""
            # 重新創造一顆brick,再各別加到視窗!!!

            if i % 10 == 0 or i % 10 == 1:
                color = 'red'
            elif i % 10 == 2 or i % 10 == 3:
                color = 'orange'
            elif i % 10 == 4 or i % 10 == 5:
                color = 'yellow'
            elif i % 10 == 6 or i % 10 == 7:
                color = 'green'
            elif i % 10 == 8 or i % 10 == 9:
                color = 'blue'
            for j in range(0, brick_cols):
                brick = GRect(brick_width, brick_height)    # We don't have to put the "brick" on "self",
                brick.filled = True                         # because a "single variable" can only store
                brick.fill_color = color                    # a "single object"
                brick.x = j * (brick_width + brick_spacing)
                brick.y = i * (brick_height + brick_spacing) + brick_offset
                self.window.add(brick)

        # Life

    def all_clear(self):  # 若消滅磚塊的次數 等於 行乘列的磚塊加總 則重製ball
        if self.all_brick == BRICK_ROWS * BRICK_COLS:
            self.reset_ball()

    def reset_ball(self):  # 重製ball到最初的原點
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.width)/2)

    def remove(self):  # 消除磚塊
        for x in range(2):
            for y in range(2):
                obj_ = self.window.get_object_at(self.ball.x + (self.ball.width*x), self.ball.y + (self.ball.height*y))
                if obj_ is not None:
                    if obj_ is self.paddle and self.__dy > 0:
                        self.__dy = -self.__dy
                    if obj_ is not self.paddle:
                        self.__dy = -self.__dy
                        self.window.remove(obj_)
                        self.all_brick += 1

    def start(self, event):  # 當滑鼠點擊後,給予球初始的速度值
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def change_x(self):
        self.__dx *= -1

    def change_y(self):
        self.__dy *= -1

    def get_velocity_x(self):
        return self.__dx

    def get_velocity_y(self):
        return self.__dy

    def paddle_move(self, event):  # 控制板子的移動
        """
        This function has the paddle move with its center following the mouse.
        :param event: MouseEvent, stores the position information where the mouse event happens.
        """

        self.paddle.x = event.x - self.paddle.width / 2  # 滑鼠游標x軸為版子的中心點
        self.paddle.y = self.window.height - PADDLE_OFFSET  # 板子的y軸始終固定
        self.window.add(self.paddle)
        if self.paddle.x >= self.window.width - self.paddle.width:  # 使板子不要超過視窗
            self.paddle.x = self.window.width - self.paddle.width
        if self.paddle.x < 0:
            self.paddle.x = 0









