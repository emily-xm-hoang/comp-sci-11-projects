# creating a module
def is_green(r,g,b):
    return 0 <= r < 25 and 230 < g <= 255 and 0 <= b < 25
               
def colour(r,g,b):
    if r < 25 and r >= 0 and g > 230 and g <=255 and b < 25 and b >= 0:
        return "green"
    else:
        return "other"