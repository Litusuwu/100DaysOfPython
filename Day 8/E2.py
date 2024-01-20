import math
def paint_calc(height, width, cover):
    var = ((height*width)/cover)
    print(f"You'll need {math.ceil(var)} cans of paint")        


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover = coverage)