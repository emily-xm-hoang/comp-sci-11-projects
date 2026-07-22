# Image Explorer Project (Project 6.7)

In this project, you'll be choosing a theme of images to analyze, and writing a program that can perform the analysis. You will provide a selection of at least 10 images fitting this theme. You'll give a score to each image based on a feature that you detect, and then rank them by this score.

The 10 images represent the types of input your program could expect to receive, and a user should reasonably be able to swap out any of the images with an image in the same theme to get a similar result.

For example, in class, we saw a jellybean quality assurance monitor, which took in photos of jellybeans, and analyzed them for percentage of each of a set of colours, then gave a report (e.g. the score could be the percentage of yellow detected).

In another scenario, we might have a grass lawn camera, which reports a score based around the ratio of brown to green grass.

Your deliverables:

- All files should be in a folder that is easy to find in your Github repository, in a folder '6.7' or similar.
- This README.md file with questions below answered.
- Your image processing program written in at least 2 python files.
- At least 10 images. Ensure that the total file size of all images is no more than 100 MB to avoid storage issues with Github.

---

## 1. Project Overview [Understanding context/defining/ideating]
- **What is the theme of the images being analyzed? What use case could this program be used for?**
  >> dashcam footage of vehicles on the road, specifically analyzing red cars
  >> could be used for road safety by implementing driving detection for the distance between the driver and car in front
  >> if too close, output tells driver to break fast/slow down to prevent rear-end/head-on collisions

- **What is the visual feature being detected?**
  >> the red pixels of the vehicles

- **Why is this feature detectable? How will you detect the feature?**
  >> the red pixels are detectable using image processing (PIL) and extracting the rgb value of every pixel 
  >> filter out the red pixels using:
    > for brighter red:
      > if r > 140 and r <= 255 and g > 0 and g <= 100 and b > 0 and b <= 100
    > for darker red:
      > if r > 45 and r <= 150 and g > 0 and g <= 45 and b > 0 and b <= 45

  >> estimates the size of the vehicle by using the min and max x/y values of the red pixels detected, as well as changing the pixels to neon green to make it more visible to the user
  >> estimate the distance between the driver and red vehicle

> *Extending signal:* The theme and visual feature detection are creative and draw connections to the real-world.

> *Extending signal:* The method of doing visual feature detection is sensible, robust, and well-defended. Cites a blog post, article, or academic paper that supports the algorithm used for feature detection.
---

## 2. Algorithmic Thinking [Prototyping/Making]
### Feature Detection Logic
- Name of function that does feature detection (e.g., `is_target_feature`):
  >> red_car
- Input(s) to the function:
  >> current pixel's rgb value
- Output of the function:
  >> true or false
- Plain‑English rule for detecting the feature:

> *Extending signal:* Feature detection uses a more advanced process, such as processing/transforming multiple pixels at a time, pre-processing or applying a filter to images, pixel grouping/region detection, etc. You MUST NOT use a python library for any feature detection; any feature detection code must be written by you. You must cite any external references used.

### Sorting and Searching (Unit 6)

Once you have calculated a score for each image, you will sort the images using the sorting algorithm taught in unit 6, then take a user input to search the data in some way (e.g., find an image that has 67% brown grass)

- Custom **selection sort** implemented? (Yes / No)
>> yes
- Custom **binary search** implemented? (Yes / No)
>> yes

---

## 3. Programming and Code Quality [Making]
- **Pixel iteration:** code correctly processes image pixels
- **Feature detection module** feature detection is written and organized in a separate, re-usable python module
- **Functions written:** code is broken up into multiple functions with clear separation of logic
- **Readability:** code is commented and has well-chosen variable names

> *Extending signal:* Clear code that is well-documented/easy-to-understand, well-structured, and efficient.

---

## 4. Testing, Efficiency, and Documentation [Testing]
### Test Evidence
- Describe at least one test you ran on `is_target_feature` and why this test demonstrates that the code works:
>> I tested my function, red_car(), by isolating pixel values, ex. (200,10,10), which returned as true. I then passed through a green pixel (100, 100, 100), which return as false.

- Describe at least one test for sorting/searching correctness and why this test demonstrates that the code works:
>> I tested my selection sort by printing out the output of my selection sort function, which is eventually assigned to sorted_scores. My function correctly ordered the scores while still pairing them with their respective images so I can later access them for my max/min % portion.

### Timing / Profiling
- Profiling is done on each of the main different sections of code. Output a report in seconds to 3 decimal places. Provide an example of the report here:
>> Time to process image 1: 2.011 secs

- What part of the program takes the longest, and why?
>> processing each image: you have to go through every pixel and extract its rgb value to determine if its red, modifying it to neon green, add it to a list of x and y coordinates, as well as determining its min/max x and y value to determine approximately where the car is and how the user should react in the current image

> *Extending signal:* Test and profiling evidence provided is comprehensive and makes a convincing case that the code is robust, efficient, and works as intended.

---

## 5. Collaboration and Process [Sharing]
- **Challenge faced:** What was a challenge you faced with this project? How did you overcome it?
>> I have an issue with detecting the all of the red pixels as per each image with varying degrees. Though I gave my red_car function multiple conditions to satisfy the different shades of red, I struggled to capture deeper shades without picking up on other miscellaneous pixels.

- **Future work:** What is a way that you could take this project even further?
>> Because of the issue discussed above, the results calculated in my program are not accurate, and it is obvious by inspection that some cars are too close (in which the user should break/slow down), though the output may say otherwise. I want to be able to revise the image processing aspect of my project so it is able to expand to wider colour ranges, which I have looked into. HSV seems to be a better alternative to RGB because it is able to pick up colours based on hues, saturation, and value. That aside, the tires and tinted windows are not red, hence weren't accounted for in my program, but are nevertheless part of the car itself. Being able to detect this (somehow) will ideally optimize my program for universal use.

### Peer Review
- Student whose work you reviewed:
>> Vivienne
- One concrete suggestion you gave and why:
>> The output of the list was difficult to read, formatting it differently

- Student who reviewed your work:
>> Vivienne
- What suggestion did you receive? What you did with that suggestion (or why you didn't use it?):
>> Prior to my revisions, I used linear search to sort through my data to find a match to the user's input, which was simpler to code. I did go back in implement binary search into that portin of my code

### Tool/Person-Use Statement (bullet-points; required for each tool/person used)
- Tool / Person:
  - Used for:
  - What I learned from the tool/person:

> *Extending signal:* Identifies clear growth and potential future growth from lessons learned through this project.
> 
> *Extending signal:* Sophisticated evidence indicates that the student collaborated effectively with a peer to improve their work, and effectively used peer feedback to improve their own work.
> 
> *Extending signal:* Demonstrates effective ability to collaborate with peers and/or external tools that improve their design, build, and/or testing processes for this project and future work.


---

## 6. Ready-to-submit Checklist
- [ ] At least 10 images relating to a theme/application
- [ ] Custom feature detection function in a separate module
- [ ] Selection sort and binary search implemented
- [ ] Timing reported in seconds to 3 decimal places
- [ ] Peer review complete (both gave and received peer feedback)
- [ ] All README sections completed

## 7. Grading

Proficient is the target. Extending signals are an indication of extending level work; not all signals are required for an extending grade. Other signals not indicated may also be worthy of an extending grade.

Your grade will be assigned a proficiency based around evidence of each of the curricular competencies demonstrated (indicated generally by square brackets []):
- Emerging: 3/10
- Developing: 6/10
- Proficient: 9/10
- Extending: 10/10


The competencies assessed are:
- Understanding context/defining/ideating
- Prototyping
- Making
- Testing
- Sharing