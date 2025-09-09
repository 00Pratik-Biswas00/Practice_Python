import math
def cal_area_circumference(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)

print(cal_area_circumference(3))