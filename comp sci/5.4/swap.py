from PIL import Image

image_jelly = Image.open("5.4/jelly_beans.png").load()

image_new = Image.open("5.4/jelly_beans.png")

width = image_new.width
height = image_new.height

def find_yellow(r,g,b):
    if r > 150 and r <= 255 and g > 150 and g <= 255 and b >= 0 and b < 100:
        return (255,255,255)
    else:
        return (r,g,b)
    
for i in range(width):
    for j in range(height):
        r = image_jelly[i,j][0]
        g = image_jelly[i,j][1]
        b = image_jelly[i,j][2]
        new_r, new_g, new_b = find_yellow(r,g,b)
        image_new.putpixel((i,j), (new_r, new_g, new_b))

image_new.save("5.4/yellowgone.png", "png")