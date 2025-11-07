from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch
from AdvGyro import AdvGyro
from Odometry import Odometry
from Action import Action
from Telemetry import Telemetry
import umath

def sound_action():
    class SoundAction(Action):
        def update(inner_self):
            Action.robot.hub.speaker.beep(440, 100)
            return True  # выполняется один раз
    return SoundAction()

def steer_action():
    class SteerAction(Action):
        def update(inner_self):
            robot = Action.robot
            robot.steer_target = min(robot.steer_limit, max(-robot.steer_limit, robot.steer_target))
            robot.steer_motor.track_target(robot.steer_target)
            return False
    return SteerAction()

def wait_action(duration_ms):
    class WaitAction(Action):
        def __init__(inner_self):
            inner_self.timer = StopWatch()

        def update(inner_self):
            return inner_self.timer.time() >= duration_ms
    return WaitAction()

def drive_to_color():
    class DriveToColorAction(Action):
        def update(inner_self):
            X, Y = Action.robot.odometry.read()
            if Action.robot.currentcheckpoint == 3 and Action.robot.clockwise == 2:
                Action.robot.clockwise = 1 - int(Action.robot.is_orange)
            if X > 0:
                return Action.robot.color_check
            else:
                return False
    return DriveToColorAction()

def drive_to_x(target_X):
    class DriveToXAction(Action):
        def update(inner_self):
            X, Y = Action.robot.odometry.read()
            if X > target_X:
                return True
            else:
                return False
    return DriveToXAction()

def drive(drive_action: Action, exit_condition: Action):
    class DriveAction(Action):
        def update(inner_self):
            drive_action.update()
            if exit_condition.update():
                return True
            return False
    return DriveAction()

def drive_using_gyro(target_angle):
    class DriveUsingGyroAction(Action):
        def update(inner_self):
            error = Action.robot.gyro.angle_read() - target_angle
            Action.robot.steer_target = error
            return True
    return DriveUsingGyroAction()

def drive_using_odom(target_X, target_Y):
    class DriveUsingOdomAction(Action):
        def update(inner_self):
            error_y = target_Y - Action.robot.odometry.read()[1]
            error_x = target_X - Action.robot.odometry.read()[0]
            target = umath.degrees(umath.atan2(error_y, error_x))
            Action.robot.error = target
            Action.robot.steer_target = Action.robot.gyro.angle_read() - target
            return True
    return DriveUsingOdomAction()

def drive_using_checkpoints():
    class DriveUsingCheckpointsAction(Action):
        def update(inner_self):
            target_X, target_Y = Action.robot.checkpoints[Action.robot.currentcheckpoint % 12]
            error_y = target_Y - Action.robot.odometry.read()[1]
            error_x = target_X - Action.robot.odometry.read()[0]
            target = umath.degrees(umath.atan2(error_y, error_x))
            Action.robot.error = target
            Action.robot.steer_target = Action.robot.gyro.angle_read() - target
            return True
    return DriveUsingCheckpointsAction()

def turn(forward, target, steer_target):
    class TurnAction(Action):
        def __init__(inner_self):
            inner_self.steer_limit = Action.robot.steer_limit
            Action.robot.steer_limit = steer_target
            Action.robot.drive_motor.dc(30 * (1 if forward else -1))
            Action.robot.steer_target = steer_target * (-1 if forward else 1)

        def update(inner_self):
            delta_angle = target - Action.robot.gyro.angle_read()
            if -0.5 < delta_angle < 0.5:
                Action.robot.steer_limit = inner_self.steer_limit
                Action.robot.drive_motor.dc(60)
                return True
            return False
    return TurnAction()

def drive_to_point(target_X, target_Y):
    class DriveToPointAction(Action):
        def update(inner_self):
            X, Y = Action.robot.odometry.read()
            deltaX = target_X - X
            deltaY = target_Y - Y
            if deltaX * deltaX + deltaY * deltaY < 10 * 10:          
                return True 
            else:
                return False
    return DriveToPointAction()

def drive_to_checkpoint():
    class DriveToPointAction(Action):
        def update(inner_self):
            X, Y = Action.robot.odometry.read()
            target_X, target_Y = Action.robot.checkpoints[Action.robot.currentcheckpoint % 12]
            deltaX = target_X - X
            deltaY = target_Y - Y
            if deltaX * deltaX + deltaY * deltaY < 15 * 15:
                Action.robot.currentcheckpoint += 1          
                return True 
            else:
                return False
    return DriveToPointAction()

def reset():
    class Reset(Action):
        def update(inner_self):
            X, Y = Action.robot.odometry.read()
            if Action.robot.clockwise == 1:
                _X = Y - 100
                _Y = 100 - X
                Action.robot.gyro.reset(Action.robot.gyro.angle_read() - Action.robot.turn_angle)
            elif Action.robot.clockwise == 0:
                _X = -100 - Y
                _Y = X - 100
                Action.robot.gyro.reset(Action.robot.gyro.angle_read() + Action.robot.turn_angle)
            Action.robot.turn_counter += 1
            Action.robot.odometry.reset(_X, _Y)
            X, Y = Action.robot.odometry.read()
            return True
    return Reset()

def stop():
    class StopAction(Action):
        def update(inner_self):
            Action.robot.drive_motor.stop()
            return True
    return StopAction()