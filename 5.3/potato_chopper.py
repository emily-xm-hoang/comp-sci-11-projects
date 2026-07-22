from PIL import Image

img_potato = Image.open("5.3/potato.png").load()
img_output = Image.open("5.3/potato.png")

width = img_output.width
height = img_output.height

def b_w(r,g,b):
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b > 230 and b <= 255:
        return 255
    return 0
for x in range(width):
    for y in range(height):
        r = img_potato[x,y][0]
        g = img_potato[x,y][1]
        b = img_potato[x,y][2]

        new = b_w(r,g,b)
        img_output.putpixel((x,y),(new, new, new))
img_output.save("5.3/scarypotato.png","png")