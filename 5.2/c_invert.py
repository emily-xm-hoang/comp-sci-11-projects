from PIL import Image

img_bread = Image.open("5.2/image.png").load()
img_output = Image.open("5.2/image.png")

width = img_output.width
height = img_output.height

for x in range(width):
    for y in range(height):
        r = img_bread[x,y][0]
        g = img_bread[x,y][1]
        b = img_bread[x,y][2]

        img_output.putpixel((x,y),((255-r),(255-g),(255-b)))
img_output.save("5.2/weird.png","png")