# Name: Odometry module
# Version: 1.0
# Author: Mukash Madi 2025/07/14

import umath

class Odometry:
    X = 0
    Y = 0

    def __init__(self, coef):
        self.coef = coef

    def read(self):
        return self.X, self.Y
    
    def write(self, angle, enc_change):
        self.X = self.X + (enc_change / self.coef) * umath.cos(umath.radians(angle))
        self.Y = self.Y + (enc_change / self.coef) * umath.sin(umath.radians(angle))

    def reset(self, x, y):
        self.X = x
        self.Y = y