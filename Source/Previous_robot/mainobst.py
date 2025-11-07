from Robot import Robot
from Action import Action, SequentialAction, ParallelAction
from Telemetry import Telemetry
from Route import route
from Sensors import *
from Movements import *


telemetry = Telemetry(500)
myrobot = Robot(telemetry)
Action.set_robot(myrobot)
myrobot.drive_motor.run(500)

actions = [
    SequentialAction([
        drive(drive_using_cam(50, 0), drive_to_color()), 
        sound_action(),
        reset(),
        drive(drive_using_cam(50, 0), drive_to_color()), 
        reset(),
        sound_action(),
        drive(drive_using_cam(50, 0), drive_to_color()),
        reset(),
        sound_action(),
        drive(drive_using_cam(50, 0), drive_to_color()),
        reset(),
        sound_action(),
        drive(drive_using_cam(50, 0), drive_to_x(0)),
        reset(),
        stop()
    ]),
    ParallelAction([
        uart_action(),
        steer_action(),
        odometry_action(),
        print_info_action(),
        camera_action(),
    ])
]

while actions:
    for action in actions[:]:
        if action.update():
            actions.remove(action)
