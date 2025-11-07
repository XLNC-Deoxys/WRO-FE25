from Robot import Robot
from Action import Action, SequentialAction, ParallelAction
from Telemetry import Telemetry
from Route import route
from Sensors import *
from Movements import *


telemetry = Telemetry(500)
myrobot = Robot(telemetry)
Action.set_robot(myrobot)
myrobot.drive_motor.run(1000)

actions = [
    SequentialAction([
        drive(drive_using_odom(50, 20), drive_to_color()), 
        sound_action(),
        reset(True),
        drive(drive_using_odom(50, 20), drive_to_color()), 
        reset(True),
        sound_action(),
        drive(drive_using_odom(50, 20), drive_to_color()),
        reset(True),
        sound_action(),
        drive(drive_using_odom(50, 20), drive_to_color()),
        reset(True),
        sound_action(),
        drive(drive_using_odom(50, 20), drive_to_x(0)),
        reset(True),
        stop()
    ]),
    ParallelAction([
        uart_action(),
        steer_action(),
        odometry_action(),
        print_info_action(),
    ])
]

while actions:
    for action in actions[:]:
        if action.update():
            actions.remove(action)
