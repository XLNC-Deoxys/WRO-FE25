from Robot import Robot
from Action import Action, SequentialAction, ParallelAction
from Telemetry import Telemetry
from Sensors import *
from Movements import *


telemetry = Telemetry(500)
myrobot = Robot(telemetry)
Action.set_robot(myrobot)
myrobot.drive_motor.run(600)

route = []
for i in range(4):
    for j in range(3):
        route.append(drive(drive_using_checkpoints(), drive_to_checkpoint()))
        route.append(sound_action())
    route.append(reset())

route = route * 3
route.insert(6, drive(drive_using_odom(75, 0), drive_to_color()))

actions = [
    SequentialAction(
        [
            turn(True, -90, 50),
            sound_action(),
            turn(False, 90, 50)

        ] + route + [stop()]
    ),
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
