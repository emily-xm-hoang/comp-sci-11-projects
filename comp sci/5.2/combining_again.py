from PIL import Image

img_kid = Image.open("5.2/kid-green.png").load()
image = Image.open("5.2/image.png").load()

img_output = Image.open("5.2/kid-green.png")

width = img_output.width
height = img_output.height

def is_green(r,g,b):
    if r > 0 and r <= 25 and g > 145 and g <= 255 and b > 0 and b <= 25:
        return True
    
for x in range(width):
    for y in range(height):
        r = img_kid[x,y][0]
        g = img_kid[x,y][1]
        b = img_kid[x,y][2]

        if is_green(r,g,b):
            image_col = image[x,y] 
            img_output.putpixel((x,y), image_col)

img_output.save("5.2/man.png","png")