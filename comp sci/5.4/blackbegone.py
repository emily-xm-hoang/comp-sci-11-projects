from PIL import Image

img_jelly = Image.open("5.4/jelly_beans.png").load()
img_output = Image.open("5.4/jelly_beans.png")

width = img_output.width
height = img_output.height

def black(r,g,b):
    if r > 0 and r <= 25 and g > 0 and g <= 25 and b > 0 and b <= 25:
        return True
    
for x in range(width):
    for y in range(height):
        r = img_jelly[x,y][0]
        g = img_jelly[x,y][1]
        b = img_jelly[x,y][2]

        if black(r,g,b):
            img_output.putpixel((x,y),(255, 255, 255))
img_output.save("5.4/blackgone.png", "png")