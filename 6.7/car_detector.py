from PIL import Image
import sys
import time
sys.path.insert(0, "6.7/red_car_module")
import module

t = []
start = time.time()
t.append(start)
all_scores = []

for i in range(1,11):
    # import images
    image_car = Image.open("6.7/cars/" + str(i) + ".png").load()
    image_new = Image.open("6.7/cars/" + str(i) + ".png")
    # find width and height
    width = image_new.width
    height = image_new.height
   
    # total of x and y coordinates that have red pixels
    total_x = []
    total_y = []
    # total number of red pixels
    total_red = 0
    # going through every pixel in each image
    for x in range(width):
        for y in range(height):
            r = image_car[x,y][0]
            g = image_car[x,y][1]
            b = image_car[x,y][2]

            if module.red_car(r,g,b):
                # if the function determines the pixel is red, make it neon green to make it visible to the user
                image_new.putpixel((x,y),(0,255,0))
                total_x.append(x)
                total_y.append(y)
                total_red += 1
    # if the total number of red pixels > 0
    if total_red > 0:
        min_x = total_x[0]
        max_x = total_x[0]
        min_y = total_y[0]
        max_y = total_y[0]
        
        # finding minimum/maximum x and y values
        for x in total_x:
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x

        for y in total_y:
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
        # area of car, NOT total image (many distractors... like the trees ;-;)
        car_area = (max_x - min_x + 1)*(max_y - min_y + 1)
        percent = round ((total_red/car_area)*100, 2)
       
    else: 
        percent = 0.0

    # print("The percent of red pixels in image " + str(i) + ": " + str(percent) + "%")
    # find center of image
    center_x = (max_x+min_x)/2
    center_y = (max_y+min_y)/2
    center = (center_x, center_y)
    if max_y > center_y:
        center_r = image_car[center][0]
        center_g = image_car[center][1]
        center_b = image_car[center][2]
        if module.red_car(center_r, center_g, center_b):
            all_scores.append((i,percent,"YOU NEED TO BREAK!!! AHAHHHHHHHHHHHHH"))
        else:
            all_scores.append((i,percent,"Beware, keep your eyes peeled..."))
    else:
        all_scores.append((i,percent,"You're good :D"))
    image_new.save("6.7/edited_pics/" + str(i) + ".png", "png")
    current_t = time.time()
    t.append(current_t)
    if i == 1:
        elapsed = round((current_t - start),3)
    else:
        elapsed = round((t[i-1] - t[i-2]),3)
    print("Time to process image " + str(i) + ": " + str(elapsed) + " secs")
    # print(all_scores)
print("\nImages\tScore (percent of red pixels)\tWhat you should do")
for current in range(1,11):
    print(str(current) + "\t" + str(all_scores[current-1][1]) + "%" + "\t\t\t\t" + str(all_scores[current-1][2]))
    # print("Image " + str(current) + " score: " + str(all_scores[current-1]) + "%")

# sort through the scores using selection sort
sort_start = time.time()

sorted_scores = module.selection_sort(all_scores)
sort_end = time.time()
sort_time = round((sort_end - sort_start),3)
print("Time to sort scores: " + str(sort_time) + " secs") 
# print(sorted_scores)
# find scores based on a range depending on user input
print("\nLet's search for a score!")
target = int(input("Pick a percentage (meow): "))

user_start = time.time()

mid = module.binary_score(sorted_scores, target)
# for a in range(1,11):
#     if sorted_scores[a-1][1] == min or sorted_scores[a-1][1] == max:
#         user.append((sorted_scores[a-1][0], sorted_scores[a-1][1]))
#     if sorted_scores[a-1][1]
    # if sorted_scores[a-1][1] >= min and sorted_scores[a-1][1] <= max:
    #     user.append((sorted_scores[a-1][0], sorted_scores[a-1][1]))
print("Images\tScore")

print(str((sorted_scores)[mid][0])+ "\t" + str((sorted_scores)[mid][1]) + "%")
user_end = time.time()
user_time = round((user_end - user_start),3)
print("Time to find scores: " + str(user_time) + " secs") 