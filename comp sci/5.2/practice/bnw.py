from PIL import Image

image_yvr = Image.open("5.2/practice/image.png").load()

image_output = Image.open("5.2/practice/image.png")

def grey(r,g,b):
    avg = int((r+g+b)/3)
    return (avg, avg, avg)

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        r = image_yvr[i,j][0]
        g = image_yvr[i,j][1]
        b = image_yvr[i,j][2]

        image_output.putpixel((i,j), (grey(r,g,b)))
image_output.save("5.2/practice/byebye.png", "png")