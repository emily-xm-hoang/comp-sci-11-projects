from PIL import Image

image_sfu = Image.open("5.3/image.png").load()

image_output = Image.open("5.3/image.png")

# remember it has to be output, not loading image
width = image_output.width
height = image_output.height

def is_light(pixel):
    avg = sum(pixel)/len(pixel)
    if avg >= 128:
        return (255,255,255)
    else:
        return (0,0,0)

for i in range(width):
    for j in range(height):
        r = image_sfu[i,j][0]
        g = image_sfu[i,j][1]
        b = image_sfu[i,j][2]
        pixel = (r,g,b)
        
        new_r, new_g, new_b = is_light(pixel)
        image_output.putpixel((i,j), (new_r, new_g, new_b))

image_output.save("5.3/newsfu.png", "png")