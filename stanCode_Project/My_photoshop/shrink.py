"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    img = SimpleImage('images/poppy.png')
    small_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            small = small_img.get_pixel(x//2, y//2)

            small.red = img_p.red
            small.green = img_p.green
            small.blue = img_p.blue
    return small_img


def main():
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
