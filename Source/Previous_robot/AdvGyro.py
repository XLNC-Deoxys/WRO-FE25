# Name: AdvGyro module
# Version: 1.0
# Author: Mukash Madi 2025/07/14

class AdvGyro:

    def __init__(self, imu):
        self.angle = 0
        self.gyro_last = 0
        self.imu = imu
        while not imu.ready:
            pass
        self.imu.reset_heading(0)
        self.reset(0)

    def angle_update(self):
        value = self.imu.heading()
        self.angle = value - self.gyro_last
        self.angle = (self.angle + 180) % 360 - 180
        return self.angle

    def angle_read(self):
        return self.angle

    def reset(self, zero_angle):
        value = self.imu.heading()
        self.gyro_last = value - zero_angle