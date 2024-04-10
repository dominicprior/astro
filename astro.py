# Calculate the XYZ dir given the alt, az, lat and long

import math
import sys

# Returns the result of rotating the vector, (x, y), anti-clockwise
# through the given angle (in degrees).

def rot(x, y, angle):
    a = math.radians(angle)
    c = math.cos(a)
    s = math.sin(a)
    return c * x - s * y, s * x + c * y

# Returns the result of rotating the vector, v, about the X axis
# clockwise through the given angle (in degrees).

def rotAboutX(v, angle):
    [x, y, z] = v
    y_, z_ = rot(y, z, angle)
    return [x, y_, z_]

# Returns the result of rotating the vector, (x, y, z), about the X axis
# clockwise through the given angle (in degrees).

def rotAboutZ(v, angle):
    [x, y, z] = v
    x_, y_ = rot(x, y, angle)
    return [x_, y_, z]

def prVec(v):
    print(f'{v[0]:,.4f}, {v[1]:,.4f}, {v[2]:,.4f}')

alt  = float(sys.argv[1])
az   = float(sys.argv[2])
lat  = float(sys.argv[3])
long = float(sys.argv[4])

v0 = [0, 1, 0]
v1 = rotAboutX(v0, alt)
prVec(v1)
v2 = rotAboutZ(v1, -az)
prVec(v2)
v3 = rotAboutX(v2, 90 - lat)
prVec(v3)
v4 = rotAboutZ(v3, 90 + long)
prVec(v4)
