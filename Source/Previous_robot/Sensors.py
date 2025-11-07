from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from AdvGyro import AdvGyro
from Odometry import Odometry
from Action import Action
from Telemetry import Telemetry
from Robot import Robot
import umath

def uart_action():
    class UartAction(Action):
        def update(inner_self):
            Action.robot.gyro.angle_update()
            Action.robot.hsv = Action.robot.color.hsv()
            Action.robot.color_check = Action.robot.hsv.s > 60
            Action.robot.is_orange = Action.robot.hsv.h > 330
            Action.robot.us_dist = Action.robot.ultrasonic.distance() / 10
            if Action.robot.us_dist > 50 and Action.robot.clockwise == 2:
                Action.robot.clockwise = True
                Action.robot.currentcheckpoint = 1
            else:
                Action.robot.clockwise = False
                Action.robot.currentcheckpoint = 2
            return False  # выполняется вечно
    return UartAction()

def odometry_action():
    class OdomAction(Action):
        def update(inner_self):
            enc = Action.robot.drive_motor.angle()
            Action.robot.enc_change = enc - Action.robot.enc_old
            Action.robot.enc_old = enc
            # if -0.5 < Action.robot.gyro.angle_read() < 0.5:
            #     Action.robot.odometry.reset(Action.robot.odometry.read()[0], Action.robot.us_dist - 47)
            Action.robot.odometry.write(Action.robot.gyro.angle_read(), Action.robot.enc_change)
            return False  # выполняется вечно
    return OdomAction()

def print_info_action():
    class PrintAction(Action):
        def update(inner_self):
            Action.robot.telemetry.set_live("X, Y: ", Action.robot.odometry.read(), "GREEN")
            Action.robot.telemetry.set_live("clockwise", Action.robot.clockwise, "YELLOW")
            Action.robot.telemetry.set_live("cam", Action.robot.camdata, "YELLOW")
            Action.robot.telemetry.set_live("abs", Action.robot.obstacle, "YELLOW")
            data = []
            for i in range(3):
                data.append(Action.robot.checkpoints[(Action.robot.currentcheckpoint % 12 // 3 * 3 + i)])
            Action.robot.telemetry.set_live("Checkpoint", [Action.robot.currentcheckpoint , data], "YELLOW")
            Action.robot.telemetry.render()
            return False  # выполняется вечно
    return PrintAction()

def camera_action():
    class CameraAction(Action):
        def update(inner_self):
            if Action.robot.currentcheckpoint > 12:
                return True
            Action.robot.camdata = Action.robot.camera.read(0)
            clr = Action.robot.camdata[4]
            if clr == 0:
                return False
            if clr == 1:
                Action.robot.hub.speaker.beep(100,100)
            else:
                Action.robot.hub.speaker.beep(300,100)
            shift = 2 - 2 * (2 - clr)
            camX = Action.robot.camdata[shift] - 4
            camY = Action.robot.camdata[1 + shift]

            poseX, poseY = Action.robot.odometry.read()
            heading = umath.radians(Action.robot.gyro.angle_read())

            # transform camera obst into world coords
            obstX = poseX + umath.cos(heading) * camX - umath.sin(heading) * camY
            obstY = poseY + umath.sin(heading) * camX + umath.cos(heading) * camY
            Action.robot.obstacle = (obstX,obstY)

            for i in range(6):
                slotX, slotY, greenY, redY = Action.robot.slots[i]
                if slotX - 20 < obstX < slotX + 20 and slotY - 10 < obstY < slotY + 10:
                    Action.robot.checkpoints[Action.robot.currentcheckpoint % 12 // 3 * 3 + i // 2][1] = greenY if clr == 1 else redY
            return False
    return CameraAction()