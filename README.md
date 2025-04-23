<div align=center>
 XLNC Deoxys team's repository for WRO Future Engineers 2025
 
 Members: Dastan Musrepov, Zhanibek Danabek, Ansar (Frosis)

 ![logo](./Images/README_photos/xCellence.jpg)
</div>

***

# Contents

* [Mobility management](#mobility-management)
  * [Motor selection](#motor-selection)
  * [Chassis design](#chassis-design)
    * [Models](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Models)
    * [Instruction](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Instruction.pdf)
* [Power and sense management](#power-and-sense-management)
  * [Power management](#power-management)
    * [Schemes](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Schemes)
  * [Sensor management](#sensor-management)
    * [Ultrasonic research](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Ultrasonic_research/README.md) 
* [Engineering factor](#engineering-factor)
* [Obstacle management](#obstacle-management)
  * [Program and pseudocode](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Source)
* [Performance video](#performance-video)
  * [Qualification]([https://youtu.be/wz5MyXlZ5nA](https://youtu.be/IbS0yFTRe58?si=sEzfAh8LpjgD5ZdR)](https://youtu.be/PEcvhSUIzB4?si=UgS1X2oOMbhzZKGW))
  * [Obstacle]([https://youtu.be/M8BKB8U_-hU](https://youtu.be/IbS0yFTRe58?si=sEzfAh8LpjgD5ZdR](https://youtu.be/IbS0yFTRe58?si=Fjd2noFWhd0FMp65))
  * [Obstacle](https://youtu.be/)
* [Pictures](#pictures)
  * [Team photos](#team-photos)
  * [Robot photos](#robot-photos)

***

# Mobility Management

## Motor selection

Comparison of motors:
The large motor runs at 160-170 rpm, with a running torque of 20 Ncm and a stall torque of 40 Ncm (slower, but stronger).
The medium motor runs at 240-250 rpm, with a running torque of 8 Ncm and a stall torque of 12 Ncm (faster, but less powerful).
We use a one medium motor for steering and two medium motors in the back for driving. We use medium motors because they are lighter, faster, more accurate and have enough torque.
<!The medium motor is lighter and is sufficient for steering, while the larger motors have more power, which helps them be the main driving force of the robot.>

## Chassis design
<div align=center>

 ![photo](./Images/README_photos/Ackermann_steering_geometry.png)
</div>



We installed all the motors vertically to make the robot smaller. Our brick is positioned with the battery forward to shift the center of gravity to the font wheels to increase treir grip. The steering motor works without gears for increased speed and precision. The width of our robot is 16 cm and the length of our robot is 15.9 cm, which allows us to park perpendicularly. Gears on the rear motors are 3:1 (excluding differential) and diameter of the wheels is 56 mm. Our robot is rear-wheel drive. This greatly simplifies the design and improves maintainability. We have a differential on the rear axle, which helps reduce the turning radius.
Last year we tried to use the Ackerman steering system ([photo above](https://github.com/RobotekPRIME2024/WRO-FE24/tree/main/Images/README_photos/Ackermann_steering_geometry.png)). The backlash was too big, we decided to abandon this mechanism this year. This allowed to increase the maximum rotation angle and simplify the design.
3D models of the robot made in BrickLink Studio 2.0 and Pixy2 mount are located in the [Models](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Models) folder. Building instructions located in the [Instruction](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Instruction.pdf) file.

тут рендер робота (когда закончиим)
<div align=center>

 <img src="./Images/Robot_photos/Batmobile.png" height="1000">
</div>
***

# Power and sense management

## Power management

The power for the EV3 Brick and the whole vehicle comes from a rechargeable 10V Lithium Battery. It (with a brick) is placed closer to the front axle than to the rear to ensure good traction of the front wheels when cornering. Schemes for each electronic part of the robot can be found [here](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Scheme.pdf).

## Sensor management

We use a color sensor to detect and determine the color of lines, a gyroscope to determine the angle of the robot, one ultrasonic sensor in the “obstacle” (clockwise or counterclockwise) or two in the “open” to determine the distance between the robot and the wall. We also use the Pixy2 Camera to detect and determine the color of road signs. On April 8, we made a graph of error versus angle. To determine the most accurate distance of the robot from the border, we conducted a research, which you can find in the [Researches](https://github.com/RobotekPRIME2024/WRO-FE24/tree/main/Ultrasonic_research). The ultrasonic sensor shows incorrect data if it is located at an angle. On April 8, we made a graph of error versus angle.

***

# Engineering factor

We used components from the MINDSTORMS EV3 Core Set, Expansion Set, a Pixy2, some other technic pieces from other sets and 3D printed [case for Pixy](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Models/Pixy2_case). List of Lego EV3 sets we use in Bricklink can be found [here](https://www.bricklink.com/catalogList.asp?catType=S&catString=166.59.800)

***

# Obstacle management

First you need to configure Pixy2 to detect green and red pillars. Then you need to find the trajectory of the pillar using the Pixy2. To do this, we launch the robot so that it goes around the pillar and records its coordinates using the Pixy2. He takes the center of the pillar as the coordinates. After that, we transfer the data into a table and use the built-in tools in Google Sheets to find the equation. If the robot sees a pillar, it tries to follow that trajectory. If the pillar is red, then x of function are multiplied by 1, and if the pillar is green, then x of function are multiplied by -1 (inverse function). Our Pixy2 camera is at angle of 45 degrees so as not to lose the object too early and to detect it far enough away. If the robot does not see the pillar, it tries to bring the ultrasonic values ​​closer to 44 cm.
<div align=center>

 ![photo](./Images/README_photos/Trajectory_of_pillar.jpg)
</div>

The final robot program with pseudocode is located in the [Source](https://github.com/XLNC-Deoxys/WRO-FE24/tree/main/Source).

***

# Performance video

Here is the link to [qualification]([https://youtu.be/](https://youtu.be/IbS0yFTRe58?si=sEzfAh8LpjgD5ZdR)](https://youtu.be/PEcvhSUIzB4?si=UgS1X2oOMbhzZKGW)) and [obstacle]([https://youtu.be/](https://youtu.be/IbS0yFTRe58?si=sEzfAh8LpjgD5ZdR)) rounds demostration.

***

# Pictures
## Team photos
![photo](./Images/Team_photos/Official.jpg)
![photo](./Images/Team_photos/Funny.jpg)

## Robot photos
![photo](./Images/Robot_photos/Gotham.png)
![photo](./Images/Robot_photos/Top.jpg)
![photo](./Images/Robot_photos/Bottom.jpg)
![photo](./Images/Robot_photos/Front.jpg)
![photo](./Images/Robot_photos/Rear.jpg)
![photo](./Images/Robot_photos/Left.jpg)
![photo](./Images/Robot_photos/Right.jpg)
