from PIL import Image

img_original = Image.open("5.2/image.png").load()

img_output = Image.open("5.2/image.png")

width = img_output.width
height = img_output.height

for x in range(width):
    for y in range(height):
        r = img_original[x,y][0]
        g = img_original[x,y][1]
        b = img_original[x,y][2]

        new = int((r+g+b)/3)
        img_output.putpixel((x,y),(new, new, new))
img_output.save("5.2/oui.png","png")