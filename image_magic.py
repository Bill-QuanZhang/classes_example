# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

# load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = image.getpixel((0, 0))  # grab pixel (0, 0)

print(a_pixel)

# Iterate over EVERY PIXEL
image_width = image.width
image_height = image.height

# Modify the image to convert it from color to gray
# (r, g, b) ---> (?, ?, ?)
# Top to bottom
for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))

        print(f"\nPixel Location: {x}, {y}")

        # red value of the pixel
        # print(f"red: {a_pixel[0]}")
        # print(f"green: {a_pixel[1]}")
        # print(f"blue: {a_pixel[2]}")

        # grab r,g b
        # red = pixel[0]
        # green = pixel[1]
        # blue = pixel[2]
        red, green, blue = pixel

        # Calculate the average
        average = int(sum(pixel)/len(pixel))
        # average = int((red + green + blue) / 3)

        # create a gray pixel
        gray_pixel = (average, average, average)
        print(gray_pixel)  # test

        # put that in the new image
        output_image.putpixel((x, y), gray_pixel)
output_image.save('grayscale.jpg')