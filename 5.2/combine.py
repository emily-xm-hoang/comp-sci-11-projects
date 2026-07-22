from PIL import Image
import sys
sys.path.insert(0, "5.2/colours")
import colours

# open beach and kid image files  
image_green = Image.open("5.2/kid-green.png").load()
image_beach = Image.open("5.2/beach.png").load()

# create output canvas
image_output = Image.open("5.2/kid-green.png")

# get the width and height of the image
width = image_output.width
height = image_output.height

# go through every pixel in the green screen
for i in range(width):
      for j in range(height):
        r = image_green[i, j][0]
        g = image_green[i, j][1]
        b = image_green[i, j][2]

        # if the pixel is green, replace it with the beach as the background
        if colours.is_green(r,g,b):
               beach_colour = image_beach [i,j]
               image_output.putpixel((i,j), beach_colour)
# save the output image
image_output.save("5.2/colouroutput.png", "png")
            