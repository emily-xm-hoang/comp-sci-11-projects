from PIL import Image


def colour(r,g,b):
    if  r > 230 and r <= 255 and g >= 0 and g < 25 and b > 230 and b <= 255: #magenta
        return "magenta"
    if  r > 230 and r <= 255 and g > 230 and g <= 255 and b >= 0 and b < 25: #yellow
        return "yellow"
    if  r > 230 and r <= 255 and g > 230 and g <= 255 and b > 230 and b <= 255: #black
        return "black"
    if  r >= 0 and r < 25 and g >= 0 and g < 25 and b >=0 and b < 25: #white
        return "yellow"
    if r > 230 and r <= 255 and g >= 0 and g < 25 and b >= 0 and b < 25: #red
        return "red"
    if r >= 0 and r < 25 and g > 230 and g <=255 and b >= 0 and b < 25: #green
        return "green"
    if r >= 0 and r < 25 and g >= 0 and g < 25 and b > 230 and b < 255: #blue
        return "blue"

image_green = Image.open("5.1/kid-green.png").load()
image_beach = Image.open("5.1/beach.png").load()

pixel = image_green[100,50]
r = pixel[0]
g = pixel[1]
b = pixel[2]

print(colour(r,g,b))