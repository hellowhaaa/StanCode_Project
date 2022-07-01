"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel_person = figure_img.get_pixel(x, y)
            pixel_background = background_img.get_pixel(x, y)
            bigger = max(pixel_person.red, pixel_person.blue)
            if bigger*2 < pixel_person.green:
                pixel_person.red = pixel_background.red
                pixel_person.blue = pixel_background.blue
                pixel_person.green = pixel_background.green
    return figure_img


def main():

    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    figure.show()
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
