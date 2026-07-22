from PIL import Image

def is_green(r, g, b):
    if r >= 0 and r < 25 and g > 230 and g <=255 and b >= 0 and b < 25:
        return True
    else: 
        return False

image_green = Image.open("5.1/kid-green.png").load()
image_beach = Image.open("5.1/beach.png").load()

print(image_green[0,0])

pixel = image_green[0,0]
r = pixel[0]
g = pixel[1]
b = pixel[2]

print("Is there green: " + str(is_green(r,g,b)))