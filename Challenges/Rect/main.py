def area_sum(rectangles):
    lyst = []
    sum_area = 0
    for rect in rectangles:
        height = rect["height"]
        width = rect["width"]
        area = height * width
        lyst.append(area)
    for i in lyst:
        sum_area = i + sum_area
    return sum_area
        