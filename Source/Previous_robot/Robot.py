from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Port, Axis, Direction
from pybricks.tools import StopWatch
from AdvGyro import AdvGyro
from Odometry import Odometry
from Action import Action
from Telemetry import Telemetry

class Robot:
    def __init__(self, telemetry):
        self.hub = PrimeHub(front_side=Axis.Y, top_side=-Axis.X)

        self.drive_motor = Motor(Port.D)
        self.drive_motor.reset_angle(0)
        self.drive_motor.control.pid(40000, 15000, 1000, 1, 100)
        self.drive_motor.control.limits(1500,500,263)

        self.color_check = 0
        self.is_orange = 0
        self.turn_angle = 90
        self.clockwise = 2  #2 if empty 1 if True and 0 if False
        self.turn_counter = 0
        self.us_dist = 0
        self.error = 0

        self.color = ColorSensor(Port.A)
        self.ultrasonic = UltrasonicSensor(Port.C)
        self.camera = PUPDevice(Port.B)
        self.gyro = AdvGyro(self.hub.imu)

        self.odometry = Odometry(42.8)
        self.odometry.reset(-37.5, -34.4)
        self.telemetry = telemetry
        self.camdata = [0,0,0,0,0,0,0,0,0]

        self.enc_change = 0
        self.enc_old = 0

        self.steer_motor = Motor(Port.F, Direction.CLOCKWISE, [1, 1], True, 5)
        self.steer_motor.control.pid(10000, 5000, 709, 8, 15)
        self.steer_limit = 50
        self.steer_target = 0

        self.checkpoints = [[0, 0] for _ in range(12)]
        self.currentcheckpoint = 1
        self.obstacle = (0,0)       
        self.slots = [
            # [slotX, slotY, greenY, redY]
            [-50, 10, -20, 30],
            [-50, -10, -30, 20],
            [0, 10, -20, 30],
            [0, -10, -30, 20],
            [50, 10, -20, 30],
            [50, -10, -30, 20]
        ]

        for i in range(4):
            self.checkpoints[i * 3] = [-50, 0]
            self.checkpoints[i * 3 + 1] = [0, 0]
            self.checkpoints[i * 3 + 2] = [50, 0]