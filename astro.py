# Calculate the XYZ dir given the alt, az, lat and long.
# The axes are:
# X going out through the equator at longitude 0
# Y going out through the equator at longitude 90 East
# Z going out through the North pole

import math
import sys

# Returns the result of rotating the vector, (x, y), anti-clockwise
# through the given angle (in degrees).

def rot(x, y, angle):
    a = math.radians(angle)
    c = math.cos(a)
    s = math.sin(a)
    return c * x - s * y, s * x + c * y

# These 3 functions return a vector that is a rotation of v about an axis by
# the angle in degrees.
# The rotation is clockwise when looking along the axis.

def rotAboutX(v, angle):
    [x, y, z] = v
    y_, z_ = rot(y, z, angle)
    return [x, y_, z_]

def rotAboutY(v, angle):
    [x, y, z] = v
    z_, x_ = rot(z, x, angle)
    return [x_, y, z_]

def rotAboutZ(v, angle):
    [x, y, z] = v
    x_, y_ = rot(x, y, angle)
    return [x_, y_, z]

def prVec(v):
    print(f'{v[0]:,.4f}, {v[1]:,.4f}, {v[2]:,.4f}')

if (len(sys.argv) != 5):
    print('\nExpects 4 args: alt, az, lat, long.')
    print('    (The args are in alphabetical order).')
    exit(1)

alt  = float(sys.argv[1])
az   = float(sys.argv[2])
lat  = float(sys.argv[3])
long = float(sys.argv[4])

v0 = [0, 0, 1]
v1 = rotAboutY(v0, alt)
# prVec(v1)
v2 = rotAboutX(v1, -az)
# prVec(v2)

# v2 is the XYZ for alt and az for someone standing at 0° latitude
# and 0° longitude.

# Then we move the person to the correct latitude and longitude.

v3 = rotAboutY(v2, -lat)
# prVec(v3)
v4 = rotAboutZ(v3, long)
prVec(v4)
