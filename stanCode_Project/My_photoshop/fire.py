"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    img = SimpleImage('images/greenland-fire.png')
    for pixel in img:
        avg = (pixel.blue + pixel.red + pixel.green) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.green = 0
            pixel.blue = 0
            pixel.red = 255
        else:
            pixel.green = avg
            pixel.blue = avg
            pixel.red = avg
    return img


def main():

    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
