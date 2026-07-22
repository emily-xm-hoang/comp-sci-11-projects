def is_light(pixel):
    avg = sum(pixel)/len(pixel)
    if avg > 128:
        return True
    else:
        return False
# pixel = (31, 215, 210)
pixel = (32, 123, 110)
print(is_light(pixel))