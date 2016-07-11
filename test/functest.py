import math

def q(a,b,c):
    x = (-b + sqrt(b * b - 4 * a * c)) / 2 / a
    y = (-b - sqrt(b * b - 4 * a * c)) / 2 / a
    return x, y

print q(2, 3, 0)
