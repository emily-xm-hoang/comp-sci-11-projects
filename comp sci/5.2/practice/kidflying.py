from PIL import Image

image_yvr = Image.open("5.2/practice/image.png").load()
image_kid = Image.open("5.2/practice/kid-green.png").load()

image_output = Image.open("5.2/practice/image.png")

width = image_output.width
height = image_output.height

def green(r,g,b):
    if r < 25 and r >= 0 and g > 230 and g <=255 and b < 25 and b >= 0:
        return True
    else:
        return False

for i in range(width):
    for j in range(height):
        r = image_kid[i,j][0]
        g = image_kid[i,j][1]
        b = image_kid[i,j][2]

        if green(r,g,b):
            yvr_r = image_yvr [i,j][0]
            yvr_g = image_yvr [i,j][1]
            yvr_b = image_yvr [i,j][2]
            image_output.putpixel((i,j),(yvr_r, yvr_g, yvr_b))

image_output.save("5.2/practice/new.png","png")