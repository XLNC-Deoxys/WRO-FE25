<div align=center>

 ![logo](./Images/README_photos/xCellence.jpg)
</div>

***

# Contents
* [The team](#the-team)
* [The challenge](#the-challenge)
* [Mobility management](#mobility-management)
  * [Platform and notors selection](#platform-selection)
  * [Chassis design](#weight-distribution)
    * [Models](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Models)
  * [BOM and assembly instructions](#components-and-building-instructions)
    * [Bill of materials](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Bill_of_materials.pdf)
    * [Instruction](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Instruction.pdf)
* [Power and sense management](#power-and-sense-management)
  * [Microcontroller selection](#microcontroller-selection)
  * [Sensor management](#sensor-management)
    * [Ultrasonic research](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Ultrasonic_research/README.md) 
  * [Power management](#power-management)
    * [Schemes](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Scheme.pdf)
* [Software](#software)
  * [Open challenge](#open-challenge)
    * [Performance video](https://youtu.be/S0fUP4UXTCI)
    * [Open program exlanation](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Open_Explanation.md)
    * [Open program pseudocode](#pseudocode)
  * [Obstacle challenge](#obstacle-challenge)
    * [Performance video](https://youtu.be/HjAzdkyZQP8)
    * [Ostacle program explanation](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Obstacle_Explanation.md)
    * [Obstacle program pseudocode](#pseudocode)
  * [Calibration program exlanation](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Calibration_Explanation.md)
* [Future plans](#future-plans)
* [Robot photos](#robot-photos)

***

# The team

We are the XLNC-Deoxys team from Kazakhstan, and we are competing in the 2025 WRO Future Engineers category.

| <img src="./Images/Team_photos/Dastan.jpg" height="300"/> | <img src="./Images/Team_photos/Zhanibek.jpg" height="500"/> |
| ---| -- |
| **Dastan Musrepov** | **Zhanibek Danabek** |
| Builder | Programmer |

# The challenge

The **[WRO 2024 Future Engineers - Self-Driving Cars](https://wro-association.org/)** challenges participants to design, build, and program an autonomous, self-driving car capable of stable navigation on a constantly changing game track. The challenge includes two tasks: driving around a circuit with changing interior walls and avoiding randomly placed obstacles based on their color, and performing a precise parallel parking maneuver at the end. Teams must utilize complex robotic systems, such as computer vision, sensor fusion, and kinematics, focusing on stability and innovation.

This challenge addresses all aspects of the engineering process, including:

* **Mobility Management**: Designing efficient vehicle propulsion mechanisms.

* **Obstacle Avoidance**: Developing a strategy for detecting and navigating road signs (red and green markers) within specified rules.

* **Documentation**: Demonstrating engineering progress, design solutions, and open-source collaboration through a publicly accessible GitHub repository.

A link to the rules can be found [here](https://wro-association.org/wp-content/uploads/WRO-2024-Future-Engineers-Self-Driving-Cars-General-Rules.pdf).

# Mobility management

<div align=center>

 ![photo](./Images/Robot_photos/Components.png)
</div>

## Platform selection

We used LEGO to build the robot because it allows rapid design and testing of mechanical and electronic solutions, ensuring stable motors, sensors, and compatibility with official controllers. This reduces assembly time and allows us to focus on autonomous driving algorithms rather than complex mechanics.

## Motor selection

| Motor | Nominal Speed (RPM) | Running Torque (N·cm) | Stall Torque (N·cm) | Mass (g) | Power Consumption (W) |
| -- | -- | -- | -- | -- | --|
| EV3 Medium Motor | 250 | 8 | 12 | 75 | 2.5 |
| EV3 Large Motor | 160 | 20 | 40 | 110 | 4.0 |

We chose 45503 medium LEGO motor for the drive and steering because they have an encoder and sufficient torque, and compared to large Lego motors, medium motors are lighter, more compact, and more accurate.

## Weight distribution
We shifted the center of gravity to the front axle by mounting the steering motor horizontally and placing the main weight of the robot—the programmable brick (311 g of 650 g)—directly above the front axle. This increased friction on the front wheels, and the turning radius was reduced by almost half compared to our first design. This robot has a high center of gravity, but this doesn't hinder it since it moves slowly.

The weight distribution of our robot by axles is 45:55 - 45% on the front and 55% on the rear axle.

## Chassis design
<p align="center">
  <img src="./Images/README_photos/Base.jpg" height="200"/>
  <img src="https://www.freeiconspng.com/uploads/red-arrow-png-22.png" width="50"/>
  <img src="./Images/README_photos/Drivetrain.jpg" height="200"/>
  <img src="https://www.freeiconspng.com/uploads/red-arrow-png-22.png" width="50"/>
  <img src="./Images/Robot_photos/Robot.jpg" height="200"/>
</p>

The main idea behind our design was simplicity.

<div align="center">
  <img height="300" alt="image" src="https://github.com/user-attachments/assets/81c020da-5f72-4560-b681-a54ecef0206b"/>
</div>

We use a LEGO differential (a new reinforced one because it does not slip and can withstand any loads) to prevent wheel slippage when turning. The operating principle of the differential is shown in the photo above.

Our robot's base consists of just two main beams, supporting both motors, the differential, the rear wheels, the steering gear, the brake, and the gyroscope. This is the simplest and lightest design, weighing only 500 grams. We believed that using printed parts would increase friction between the moving parts, complicate the design, and increase the weight of the robot.

We selected the diameter of the wheels so that the robot's design would be as simple as possible and the robot would be perpendicular to the ground for the correctness of the gyroscope value.

We tried to make the base as short as possible to reduce the turning radius. However, this resulted in a significantly increased front overhang (6 cm) compared to our previous robot (1 cm). Our robot's dimensions are 29 x 9 x 26.5 cm. This means we utilize the full permitted length and height.

## Ackerman steering geometry

| ![photo](./Images/README_photos/Ackermann_steering.jpg) | ![photo](./Images/README_photos/Parallel_steering.jpg) |
| :---: | :---: |
| **Ackerman steering** | **Parallel steering** |

After extensive testing of the Ackerman steering geometry, we decided to go with parallel steering, as the Ackerman steering design significantly reduces the maximum steering angle of the wheels, and the play in the LEGO parts makes it less precise, especially in the micro-movements we use constantly throughout the program. One of the reasons for the ineffectiveness of the Ackerman steering system in our case is the size, weight, and speed of the robot. At such a small scale, the absence of a steering system is not critical, as both systems will behave identically.

To compensate for the lack of an Ackermann system and enable a maximum turning angle of up to 70 degrees without bouncing or abrupt movements, we installed thin wheels on the front axle. When turning at such a large angle, they slide slightly on the surface, allowing for a significantly smaller turning radius without sacrificing smoothness, precision, or compactness.

## Camera Positioning

We moved the camera as far back as possible (by 17.6 cm from the center) and upward (by 27 cm from the ground) for a better view and to keep obstacles in sight for a long time. This also lengthens the robot and, consequently, the parking area.

<div align="center">
  <img src="./Images/README_photos/Pythagorean_camera_mount.png" width="500"/>
</div>

The camera mount is designed to be as light and sturdy as possible, as otherwise the camera will wobble and the robot will move crookedly. The lever created by the huge distance between the base and the camera will put pressure on the rear axle, impairing maneuverability. To achieve these goals, we used the Pythagorean theorem in beam connections (8, 15, 17). Our camera mount allows for quick adjustment of its angle.

## Old designs

<div align="center">
  <img src="./Images/Robot_photos/Nationals_robot.jpg" width="300"/>
</div>

At the regional and national stages, we also used the EV3, but we tried to build the shortest and fastest robot possible for parking and rapid qualification. It was shorter by 12 cm but wider by 6 cm.

| Advantages | shorter | lower center of gravity | easier battery changes |
| -- | -- | -- | -- |
| Disadvantages | wider | less accurate odometry |  | 

<div align="center">
  <img src="./Images/Robot_photos/Training_camp_robot.jpg" width="300"/>
</div>

Then, during training camp, we switched to a new platform – the LEGO Spike Prime. It turned out to be the smallest we've ever built: approximately 10 x 10 cm. Our camera protruded 15 cm back, which made parking incredibly easy, but due to the ban on parking simplifications by driving over it, this compact design was pointless. For this design, we used the OpenMV H7 Plus camera, which, as it turned out, has a small field of view. Therefore, we had to use crutches and pinpoint the exact position of the obstacle using a SLAM unit.

| Advantages | smallest (fits in a pocket) | large number of iterations thanks to a powerful brick and pybricks | smallest turning radius |
| -- | -- | -- | -- |
| Disadvantages | doesn't comply with new regulations | camera field of view is too small | |

<!--
<div align=center>
 
 ![photo](./Images/README_photos/Size_comparison.jpg)
</div>
-->

## Components and building instructions

We used parts from the standard EV3 and Spike Prime kits (дополнииить), as well as a Pixy2 camera, which can be ordered ([here](https://www.dfrobot.com/product-1752.html)), a 3D model of which, along with a printed case, can be found [here](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Models). You can find our bill of materials [here](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Bill_of_materials.pdf). You can find the assembly instructions [here](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Instruction.pdf).

***

# Power and sense management

## Microcontroller selection

We chose EV3 as a main microcontroller because:

1) LEGO Mindstorms EV3 has official sensors whose quality and reliability we're confident in, as well as sensors and modules from third-party manufacturers (such as Pixie) that support LEGO Mindstorms EV3 without any additional workarounds.
2) Unlike the 3D-printed parts found in robots using Arduino and Raspberry Pi, LEGO construction can be quickly and easily changed.

| | ![photo](https://ir.ozone.ru/s3/multimedia-4/c400/6121045792.jpg) | ![photo](https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt319a240f7e71b963/5fb4f19cffb61e50a0fad8f2/45601_prod_01-2c6c9e81a6e5e5e17b3b3e3ff2c803ad.png?locale=en-us) | ![photo](https://www.sparkfun.com/media/catalog/product/cache/a793f13fd3d678cea13d28206895ba0c/D/E/DEV-26125-Raspberry-Pi-5-2G-Feature2.jpg) | ![photo](https://store.arduino.cc/cdn/shop/files/A000066_03.front_1200x600_crop_center.jpg?v=1727098250) | ![photo](https://developer.nvidia.com/blog/wp-content/uploads/2019/03/Jetson-Nano_3QTR-Front_Left-1920px.png) |
| -- | -- | -- | -- | -- | -- |
| Parameter | **LEGO EV3** | **LEGO SPIKE Prime** | **Raspberry Pi 5** | **Arduino Uno R3** | **NVIDIA Jetson Nano** |
| **Processor / MCU** | ARM9 300 MHz | ARM Cortex-A7 528 MHz | Broadcom BCM2712 (4 × Cortex-A76 2.4 GHz) | ATmega328P (8-bit 16 MHz) | Quad-core ARM A57 1.43 GHz + GPU 128 CUDA |
| **RAM** | 64 MB | 64 MB | 4–8 GB | 2 KB | 4 GB |
| **Storage / SD Card** | microSD up to 32 GB | Built-in + microSD | microSD or SSD M.2 | None | microSD up to 128 GB |
| **I/O Interfaces** | 4 motor ports / 4 sensor ports | 6 universal ports | 40 GPIO | 14 GPIO | 40 GPIO |
| **Sensor / Module Support** | LEGO EV3 / NXT sensors / PixyCam2 | LEGO SPIKE / Powered Up sensors | Any (Cameras, IMU, LiDAR, GPS etc.) | Analog / digital basic sensors | Cameras, LiDAR, IMU, AI modules |
| **Computer Vision Support** | No (limited) | No (limited) | Yes (OpenCV, TensorFlow Lite, AI models) | No | Yes (OpenCV, PyTorch, TensorRT) |
| **Programming Languages** | EV3-G, Basic (CLEV3R) | Scratch, Python (Pybricks) | Python, C++, ROS, OpenCV | C/C++ (Arduino IDE) | Python, C++, CUDA, ROS |
| **Development Complexity** | Low | Low | Medium-High | Low | High |
| **Approx. Price** | ≈ 250 USD | ≈ 400 USD | ≈ 150 USD | ≈ 25 USD | ≈ 250 USD |
| **Power Supply** | EV3 battery | SPIKE battery | USB-C 5V 5A | 9V / USB | 5V 4A |
| **Advantages** | Easy to use, reliable, ready-made sensors | Quick assembly, modern interface, BLE | Full computer, AI capabilities, OpenCV | Very cheap and simple | High performance, neural network processing, GPU |
| **Disadvantages** | Limited speed and memory | Limited custom library support | Requires setup and cooling | No storage, very low power | High power consumption, requires cooling |

## Sensor management

<div align=center>

 ![photo](./Schemes/Wiring_diagram.jpg)
</div>

We use sensors for more stable driving. We use an EV3 color sensor to detect lines and determine their color, an EV3 gyroscope for precise 90-degree turns, and an EV3 ultrasonic sensor to maintain distance to the wall and detect parking. On Qualification, we have two sensors facing in different directions, and on the Obstacle Challenge, we use a single ultrasonic sensor due to a lack of ports.

We use PID for steering, PD fo gyroscope and P regulator for the center function. It helps us to drive smoothly.

To determine the most accurate distance the robot can get from a boundary, we conducted a study, which you can read in the [Researches](https://github.com/RobotekPRIME2024/WRO-FE24/tree/main/Ultrasonic_research) folder. The ultrasonic sensor provides inaccurate data if it's positioned at an angle. On April 8th, we plotted a graph showing the error as a function of angle. To more accurately determine the distance to the wall, we use the ultrasonic sensor's readings using the formula. This is how the results of this study look in the program:

https://github.com/XLNC-Deoxys/WRO-FE25/blob/b088995db966b68d1054305769dda0a999a03505/Source/Open.bp#L122

We also tested a scanning ultrasonic sensor system, but found that it greatly complicates the code and makes the robot larger, but doesn't provide much benefit compared to a conventional distance sensor.

For maximum stability, the EV3 gyroscope and EV3 ultrasonic sensor complement each other, preventing the car from crashing into a wall even if one of them begins to show errors.

The motor encoders and gyroscope allow us to use odometry, which we used during training camp. We made a special [module](https://github.com/XLNC-Deoxys/WRO-FE25/blob/b088995db966b68d1054305769dda0a999a03505/Source/Odometry.bpm) to calculate the robot's position using this formula:

<div align="center">
 
$x_{new}=x_{old}+\cos(\theta_{old})$

$y_{new}=y_{old}+\sin(\theta_{old})$
</div>

However, we abandoned it this time because it's rather inaccurate, complicates the program, and can be omitted. Odometry's advantage is only in unexpected situations, where it greatly expands capabilities and speeds up programming.

### EV3 Gyro Sensor
<table><tr>
<td style="vertical-align:top; width:260px;">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShVLaq4yX3a_XZXLg6bj4JeahPYHT_Sgd4vg&s" alt="EV3 Gyro Sensor" width="250">
</td>
<td style="vertical-align:top;">

<p><strong>Function:</strong> Measures heading and turns for accurate angle tracking.</p>

<p><strong>Range:</strong> ±440 °/s.</p>

<p><strong>Accuracy:</strong> ±3 °.</p>

<p><strong>Outputs:</strong> Angle (°) and Rate (°/s).</p>

<p><strong>Protocol:</strong> UART.</p>

</td></tr></table>
<hr>

### EV3 Color Sensor
<table><tr>
<td style="vertical-align:top; width:260px;">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQNlzUqSe927BoohXxVIFc3oVo2a3wWcOZ4g&s" alt="EV3 Color Sensor" width="250">
</td>
<td style="vertical-align:top;">

<p><strong>Function:</strong> Detects lines and classifies surface colors for reliable navigation.</p>

<p><strong>Modes:</strong> Color (8 colors), Reflected Light, Ambient Light.</p>

<p><strong>Range:</strong> 0–100 % light intensity, effective up to ~1 cm.</p>

<p><strong>Protocol:</strong> UART.</p>

</td></tr></table>
<hr>

### EV3 Ultrasonic Sensor
<table><tr>
<td style="vertical-align:top; width:260px;">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrTvZApLOg5_8i8IpeFf9beWsCTZDxEnlK6g&s" alt="EV3 Ultrasonic Sensor" width="250">
</td>
<td style="vertical-align:top;">

<p><strong>Function:</strong> Measures wall distance, enables centering and detecting the parking zone.</p>

<p><strong>Range:</strong> 3 cm – 250 cm.</p>

<p><strong>Accuracy:</strong> ±1 cm.</p>

<p><strong>Protocol:</strong> UART.</p>

</td></tr></table>
<hr>

### PixyCam 2.1 LEGO Edition
<table><tr>
<td style="vertical-align:top; width:260px;">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfBt_ALMGtvRIdpUoeXaM-nic1FP6QZ9pm8g&s" alt="PixyCam 2.1 LEGO Edition" width="250">
</td>
<td style="vertical-align:top;">

<p><strong>Function:</strong> Detects red/green obstacles for color + position-based path planning.</p>

<p><strong>Processor:</strong> NXP LPC4330, dual-core ARM Cortex-M4 @ 204 MHz.</p>

<p><strong>Image Sensor:</strong> Omnivision OV9282 (1/4″ CMOS Global Shutter).</p>

<p><strong>Resolution:</strong> 640 × 400 pixels.</p>

<p><strong>Frame Rate:</strong> Up to 60 frames per second.</p>

<p><strong>Lens FOV:</strong> 60° horizontal × 40° vertical.</p>

<p><strong>Protocol:</strong> I2C.</p>

<p><strong>Recognition Modes:</strong> Color Signature Tracking (up to 7), Line / Intersection Detection, Barcode / Arrow Detection.</p>

<p><strong>LEGO Compatibility:</strong> Direct plug-and-play with LEGO EV3.</p>

<p><strong>Lighting:</strong> Integrated RGB LED for auto exposure feedback.</p>

<p><strong>Power Supply:</strong> 5 V @ 150 mA (via LEGO port or USB).</p>

<p><strong>Dimensions:</strong> 50 × 40 × 36 mm.</p>

<p><strong>Weight:</strong> &lt; 30 g.</p>

</td></tr></table>

## Schemes

Power Schemes for every electronic part of the vehicle can be found here:

[EV3 P-Brick](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Schemes/LEGO%2095646c01%20Programmable%20brick.pdf)

[EV3 Medium motor](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Schemes/LEGO%2099455%20Medium%20motor.pdf)

[Battery](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Schemes/LEGO%2095656%20Rechargeable%20battery.pdf)

[Color Sensor](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Schemes/LEGO%2095650%20Color%20sensor.pdf)

[Gyro sensor](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Schemes/LEGO%2099380%20Gyro%20sensor.pdf)

[Ultrasonic sensor](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Schemes/LEGO%2095652%20Ultrasonic%20sensor.pdf)

[Pixy2](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Schemes/Pixy2.pdf)

## Power management
We used the rechargeable lithium-ion battery included with the LEGO Mindstorms EV3 as a power source. Although regular AA batteries hold a charge longer, they cannot be recharged, which is critical during competitions. Before each launch, we check that the battery is fully charged, and we have an extra full battery in reserve.

### Robot power consumption

| Component | Voltage | Current (typ) | Power |
| -- | -- | -- | -- |
| 2× EV3 Medium Motors | 7.4 V | ~0.50 A | ~3.7 W |
| 2× Ultrasonic Sensors | 5 V | ~60 mA | ~0.3 W |
| Gyro Sensor | 5 V | ~10 mA | ~0.05 W |
| Color Sensor | 5 V | ~45 mA | ~0.23 W |
| Pixy2.1 Camera | 5 V | ~140 mA | ~0.7 W |
| EV3 Brick (CPU, LCD) | 7.4 V | ~0.10 A | ~0.74 W |

**Total:** ≈ 5.7 W  
**Total Current (from 7.4 V battery):** ≈ 0.8 A  
**Expected runtime (2050 mAh Li-ion):** ~2.5 hours  


***

# Software

## Calibration

We frequently ran into the issue of lightning during our tests and previous competitions. External factors like difference in lightning or even the material that the playing field is made of can affect the accuracy of the EV3 color sensor. Though we try to compensate by increasing the range at which it detects blue and orange, there is still a negative effect. To solve this, our team has a short program we launch before every run. The program simply drives forward and detects spikes in color signatures. We place the robot in a way so that it passes over both lines. It then selects the average value for both blue and orange and saves it into its storage. This value is the color value we use when detecting the line in both Open Challenge and Obstacle Challenge. In short, this calibration program allows us to mitigate external factors and improve color sensor accuracy.

## Open challenge

To help you better understand what I'm explaining, you can [click here](https://youtu.be/S0fUP4UXTCI) to view the video we created.

<div align="center">
  <a href="https://youtu.be/S0fUP4UXTCI">
    <img src="https://github.com/ThanyawutII/Test-2/blob/main/dgddv.png" width="600">
  </a>
</div>

Our team has decided to employ a simple strategy for completing the "open" round. The driving system itself uses a combination of the onboard gyroscope and ultrasonic sensor. The ultrasonic sensor measures the distance to the outer/inner wall and the robot attempts to maintain a certain distance (stored in a variable) from that wall. The gyroscope allows it to maintain a straight trajectory forward with minimum deviation. During the very first turn of the round, our robot scans the first line it passes over using a colour sensor and stores its value in a variable. This one-time operation tells our program if the robot is going clockwise or counter-clockwise (orange for clockwise and blue for counter-clockwise). This information then affects all the turns going forward, deciding whether the robot turns left or right by changing the desired turn angle to negative or vice-versa. Those turns are executed by changing the desired angle to 90 or -90 in our gyroscope function. The robot also uses a variable as a counter to check how many lines it has passed. Once that variable is equal to 12 (which means that all 3 laps are finished) the robot drives forward for a set period of time to land in its starting area and stops.

<div align=center>

 ![photo](./Images/README_photos/Detour_obstacle.png)
</div>

You can find a full breakdown of our program [here](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Open.bp).

### Pseudocode

https://github.com/XLNC-Deoxys/WRO-FE25/blob/bd55527a0a10d21631e3801bc8ee9256934dbde7/Source/Open_pseudocode.py#L1-L43

## Obstacle challenge

### Pixy2

We use a Pixy2 camera to detect obstacles and determine their color. This camera is designed specifically for use with LEGO Mindstorms EV3, so it's very easy to connect and get started. We use ([Pixymon](https://github.com/charmedlabs/pixy2/raw/master/releases/pixymon_windows/pixymon_v2_windows-3.0.24.exe)) to configure the camera. A guide on setting up the camera can be found ([here](https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:teach_pixy_an_object_2)).
1) First, we simply drive past the obstacle and record its coordinates from the camera.
2) Then we transfer these values ​​to Google Sheets and find the best fit line. Our sheet with the function calculation can be found [here](https://docs.google.com/spreadsheets/d/1uQ3p7Dw0eju2VstwOmTVAWoVSMLZkzuku79VgqmB5RI).
3) Then we insert it into the code and write the logic so that the robot tries to drive so that the obstacle's coordinates from the camera match the graph.

Our trajectory of the obstacle (Ignore the inaccuracy at the end, the camera was poorly adjusted)

<div align="center">
 
| <img src="./Images/README_photos/Red_obstacle_trajectory.jpg" height="500"/> | <img src="./Images/README_photos/Green_obstacle_trajectory.jpg" height="500"/> |
| ---| -- |
| **Trajectory of the red obstacle** | **Trajectory of the green obstacle (just reversed red trajectory)** |
</div>

### Strategy

To help you better understand what I'm explaining, you can [click here](https://youtu.be/HjAzdkyZQP8) to view the video we created.

<div align="center">
  <a href="https://youtu.be/HjAzdkyZQP8">
    <img src="https://github.com/ThanyawutII/Test-2/blob/main/dgddv.png" width="600">
  </a>
</div>

While there is no obstacle in the camera's field of view, our robot behaves similarly to the qualification run: maintaining a constant distance from the wall using an ultrasonic sensor and staying on track as well as making turns using a gyroscope.
As soon as an obstacle enters the camera's field of view, the robot switches to detour mode. For detouring, we have created a predefined function in the form of kx+b with carefully calibrated coefficients. This line acts as the ideal path that the center of the detected obstacle needs to follow in the image frame. In short, we define where the obstacle should "appear" on the camera as the robot moves in a ideal situation.
Using our "detour line" and the obstacle's XY position in the image frame, our robot can calculate the deviation of the obstacle from the ideal path and adjust its steering accordingly. This method provides our robot with consistency and ease of modification, due to the fact that every detour is mathematically identical and the coefficients of our ideal path can be changed with little effort to adapt to various situations.

You can find a full breakdown of our program [here](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Obstacle.bp).

#### Parking

Once our robot has completed the required 3 laps, we start the parking algorithm. After the last turn, we slow down movement and drive until the ultrasonic sensor detects the "left" wall of the parking zone. During this drive, the same principle as in the qualification rounds applies, the robot attempts to stay within a certain distance from the outer wall).

<div align=center>

 ![photo](./Images/README_photos/Search_for_parking.png)
</div>

As soon as the parking zone's wall is detected, the robot drives forward slightly before performing a predefined set of odometry maneuvers that land it safely inside the parking zone.

<div align=center>

 ![photo](./Images/README_photos/Parking_trajectory.png)
</div>

As you may have deduced, the above explanation only applies to counter-clockwise movement, as our primary ultrasonic sensor is located to the right of the robot and without it the detection of the parking zone is impossible. The solution to this, however, is simple. When driving clockwise, after finishing the final lap, the robot drives forward and performs a U-Turn, resulting in its position and direction being similar to its position during the beginning of our counter-clockwise parking algorithm (with negligible deviation). Once the U-Turn is performed, the robot applies that same counter-clockwise parking algorithm.

## Pseudocode

https://github.com/XLNC-Deoxys/WRO-FE25/blob/882e710d82f4d48ad58d8104a71475b1f2c5b51d/Source/Obstacle_pseudocode.py#L1-L46

***

# Future plans

## New microcontroller (Raspberry Pi)

Despite its simplicity, using LEGO poses many limitations:
1) **Number of ports:** The EV3 brick only has 4 sensor ports and 4 motor ports, so this year we only had to install one ultrasonic sensor for the obstakl.
2) **Size and weight:** The LEGO Mindstorms EV3 brick is almost half the weight of our robot (311 of 670 g). All the sensors and motors for LEGO are very large.
3) **Сomputing power:** The Raspberry Pi has a 5x higher frequency and 4 cores than the LEGO EV3. This allows for more iterations in odometry.
4) **Compatibility:** Unfortunately, the sensors and cameras compatible with LEGO are far from the best. The Raspberry Pi is much more flexible in this regard, as you can connect anything to it. This allows us to use the most accurate and fastest sensors and cameras.

## 3D printed parts

Our robot is made entirely of LEGO pieces, but the downside of moving parts made of Lego is that they weren't designed for precision mechanisms. The motor axles, gears, and differential are made of Lego and have some play. By eliminating this, we can greatly improve the precision of the steering mechanism and drive. Printed parts also make the structure more robust.

## Odometry
Our team has also experimented thoroughly with odometry. One version of our program (the SPIKE version) used a full odometry system to complete both the obstacle and open runs. You can check its program [here](https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Source/Previous_robot). Initially, we explored it because it would make adapting to surprise rules easier, however, the error propagation caused instability in later laps, which is why we decided to abandon it. We are currently attempting to integrate odometry into our parking algorithm to enhance precision and prevent wall-bumps.

***

# Robot photos

<div align="center">
  <table>
    <tr align="center">
      <td><img src="./Images/Robot_photos/Top.jpg" alt="Robot Photo 1" width="100%"></td>
      <td><img src="./Images/Robot_photos/Front.jpg" alt="Robot Photo 2" width="100%"></td>
      <td><img src="./Images/Robot_photos/Left.jpg" alt="Robot Photo 3" width="100%"></td>
    </tr>
    <tr align="center">
      <td><img src="./Images/Robot_photos/Bottom.jpg" alt="Robot Photo 4" width="100%"></td>
      <td><img src="./Images/Robot_photos/Rear.jpg" alt="Robot Photo 5" width="100%"></td>
      <td><img src="./Images/Robot_photos/Right.jpg" alt="Robot Photo 6" width="100%"></td>
    </tr>
  </table>
</div>

  <li>You can see a photos of the robot <a href="https://github.com/XLNC-Deoxys/WRO-FE25/tree/main/Images/Robot_photos" target="_blank">here</a></li>
