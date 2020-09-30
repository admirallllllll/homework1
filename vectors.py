import math
dim = input()
if dim == '2D':
    x, y = (float(i) for i in input().split())
    length = (x ** 2 + y ** 2) ** 0.5
    constant = float(input())
    x *= constant
    y *= constant
    angle = math.radians(float(input()))
    x2 = x * math.cos(angle) - y * math.sin(angle)
    y2 = x * math.sin(angle) + y * math.cos(angle)
    vector2 = [x2, y2]
    print('length: %s' %length, 'scaled ', x, ' ', y, ' ', 'new vector: ', *vector2)
else:
    x, y, z = (float(i) for i in input().split())
    length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    constant = float(input())
    x *= constant
    y *= constant
    z *= constant
    angle = math.radians(float(input()))
    axis = input()
    if axis == 'X':
        x2 = x
        y2 = y * math.cos(angle) - z * math.sin(angle)
        z2 = y * math.sin(angle) + z * math.cos(angle)
    elif axis == 'Y':
        x2 = x * math.cos(angle) + z * math.sin(angle)
        y2 = y
        z2 = z * math.cos(angle) - x * math.sin(angle)
    else:
        x2 = x * math.cos(angle) - y * math.sin(angle)
        y2 = x * math.sin(angle) + y * math.sin(angle)
        z2 = z
    vector2 = [x2, y2, z2]
    print('length: %s' % length, 'scaled ', x, ' ', y, ' ', z, ' ', 'new vector: ', *vector2)
