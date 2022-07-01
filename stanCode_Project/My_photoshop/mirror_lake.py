"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    img = SimpleImage('images/mt-rainier.jpg')
    big_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_p1 = img.get_pixel(x, y)
            big_img_p1 = big_img.get_pixel(x, y)
            big_img_p2 = big_img.get_pixel(x, big_img.height-1-y)

            big_img_p1.red = img_p1.red
            big_img_p1.green = img_p1.green
            big_img_p1.blue = img_p1.blue

            big_img_p2.red = img_p1.red
            big_img_p2.green = img_p1.green
            big_img_p2.blue = img_p1.blue
    return big_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
