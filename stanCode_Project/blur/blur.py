"""
File: blur.py
Name: Lina Chou
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(old_img):
    img = SimpleImage("images/smiley-face.png")
    blank_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            sum_g = 0
            sum_r = 0
            sum_b = 0
            times = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            sum_r += pixel.red
                            sum_g += pixel.green
                            sum_b += pixel.blue
                            times += 1
            new_pixel = blank_img.get_pixel(x, y)
            new_pixel.red = sum_r / times
            new_pixel.blue = sum_b / times
            new_pixel.green = sum_g / times
    return blank_img


def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(old_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
