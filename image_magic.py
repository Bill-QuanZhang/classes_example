# Image Magic
# Load an image and manipulate the pixels

from PIL import Image


def to_greyscale(pixel: tuple, algo="average") -> tuple:
    """Convert a pixel to greyscale.
    Can also specify the greyscale algorithm
    Defaults to average.

    Args:
        pixel: a 3-tuple of ints from
            0 - 255, e.g. (142, 54, 53)
            represents (red, green, blue)
        algo : the greyscale conversion algorithm
            specified by the user
            valid values are "average", "luma"
            defaults to "average"

    Returns:
        a 3-tuple pixel (r, g, b) in
        greyscale
    """
    # grab r,g b
    # red = pixel[0]
    # green = pixel[1]
    # blue = pixel[2]
    red, green, blue = pixel

    # Calculate the average / grey pixel
    if algo.lower() == "luma":
        grey = int(red * 0.3 + green * 0.59 + blue * 0.11)
    else:
        # average = int(sum(pixel) / len(pixel))
        grey = int((red + green + blue) / 3)

    # create a grey pixel
    # grey_pixel = (average, average, average)
    # print(grey_pixel)  # test

    return grey, grey, grey


def to_greyscale_luma(pixel: tuple) -> tuple:
    """Convert a pixel to greyscale.

        Args:
            pixel: a 3-tuple of ints from
                0 - 255, e.g. (142, 54, 53)
                represents (red, green, blue)

        Returns:
            a 3-tuple pixel (r, g, b) in
            greyscale
        """

    red, green, blue = pixel

    grey = int(red * 0.3 + green * 0.59 + blue * 0.11)

    return grey, grey, grey


# load the image (pumpkin)
# Open an output image that's the same size
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = image.getpixel((0, 0))  # grey pixel (0, 0)

print(a_pixel)

# Iterate over EVERY PIXEL
image_width = image.width
image_height = image.height

# Modify the image to convert it from color to grey
# (r, g, b) ---> (?, ?, ?)
# Top to bottom
for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        this_pixel = image.getpixel((x, y))

        # print(f"\nPixel Location: {x}, {y}")

        # red value of the pixel
        # print(f"red: {a_pixel[0]}")
        # print(f"green: {a_pixel[1]}")
        # print(f"blue: {a_pixel[2]}")

        # add function call to to_greyscale()
        grey_pixel = to_greyscale(this_pixel, "luma")
        # grey_pixel = to_greyscale_luma(this_pixel)

        # put that in the new image
        output_image.putpixel((x, y), grey_pixel)
output_image.save('greyscale_luma2.jpg')
