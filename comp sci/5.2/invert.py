from PIL import Image

def invert(r, g, b):
    return (255-r, 255-g, 255-b)

# open beach 
image_beach = Image.open("5.2/beach.png").load()

# create output canvas
image_output = Image.open("5.2/beach.png")

# get the width and height of the image
width = image_output.width
height = image_output.height

# go through every pixel
for i in range(width):
    for j in range(height):
        r = image_beach[i, j][0]
        g = image_beach[i, j][1]
        b = image_beach[i, j][2]
    
        new_r, new_g, new_b = invert(r,g,b)
        image_output.putpixel((i,j), (new_r, new_g, new_b))

# save the output image
image_output.save("5.2/invertoutput.png", "png")
            