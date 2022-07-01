"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.25


def main():
    fig = SimpleImage('S__37093382.jpg')
    bg = SimpleImage('background.jpg')
    bg.make_as_big_as(fig)
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue) // 3
            if fig_pixel.green > avg * THRESHOLD and total > 100:
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.blue = bg_pixel.blue
                fig_pixel.green = bg_pixel.green
    return fig


if __name__ == '__main__':
    main()
