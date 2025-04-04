***

**Official repository of the Robotek Lumino team from Kazakhstan. It contains all the engineering materials of our self-driven vehicle's model participating in the WRO Future Engineers competition in the season of 2024.**

***

<div align=center>

![logo](./img/Lumino.png)

</div>


## Our vehicle: 
![vehph](./img/main_robot.png)

We used components from a EV3 MINDSTORMS Educational kit + a Pixy v2.1   Camera and some other technic pieces from other sets. 

A full list of all the components (not including the camera) can be found here: [Part List](models/robot_partlist.pdf)

Instructions for assembling the robot: [Instructions](models/robot_instruction.pdf)

A 3D model of the robot made in Studio 2.0 can be found here: [3D Model](models/LuminoRobot.io)

The final program/code for our autonomous vehicle can be found here: [Program](src)
***

## Content

* `models` — contains 3д models of our robot, a case for the camera and instructions for assembling the robot.
* `schemes` — contains electrical diagrams of the battery, camera, sensors, and the main EV3 block.
* `src` — this is where the code for our robot is located.
* `t-photos` — contains two team photos (official photo and a fun team photo).
* `v-photos` — contains six photos of the car (views from all sides, top and bottom).
* `research` — a section with research that we conducted during the preparation stage for the competition. There is research on various topics such as Ackermann angle, odometry, etc.

## Contents

* [**Mobility Management**](#mobility-management)
  * [Motor Selection and Implementation](#1---selection-of-motors-and-drive-system)
  * [Steering mechanism with Ackermann angle](#steering-mechanism-with-ackermann-angle)
  * [3D Printing parts:](#3d-printing-parts)
  * [Differential Gear](#2---differential-gear)
  * [Weight Distribution](#weight-distribution) 

* [**Power and Sense Management**](#power-and-sense-management)
  * [Sensor Management](#sensor-management)
  * [Power Management](#power-management)
  * [Sensors](#more-details-about-each-sensor-and-its-power-supply-circuit-can-be-found-here) 

* [**Obstacle Management**](#obstacle-management)
  * [Coordinate System and Robot Position Correction](#coordinate-system-and-robot-position-correction)
  * [Computer Vision](#computer-vision)
  * [Trajectory Calibration](#trajectory-calibration)
  * [Parking Algorithm](#parking-algorithm)

* [**Photos**](#photos)
  * [Team Photos](#team-photos)
  * [Vehicle Photos](#vehicle-photos)

* [**Performance Videos**](#performance-videos)

* [**Problems when preparing for competitions**](#problems-when-preparing-for-competitions)

* [**Conclusion**](#conclusion)
  * [Limitations of Our Platform](#limitations-of-our-platform)
  * [Suggestions for Further Development](#suggestions-for-further-development)

<h1>Introduction</h1>
<p>The task we decided to solve is the creation of an autonomous car capable of driving laps on a track, avoiding colored obstacles depending on their color, searching and parking in a designated area. For this, we used the Pixy v2.1 camera.

As for the code, we used the LEGO Mindstorms platform to write the program for the robot, as this is the main programming environment for the EV3. LEGO Mindstorms provides a convenient graphical interface and a set of blocks that allow you to easily implement movement logic, interaction with sensors and motor control. Using this environment, we wrote code to perform the necessary tasks, such as recognizing and avoiding colored obstacles, as well as precise parking in the designated area.</p>

  
## Mobility Management 

### 1 - Selection of motors and drive system


Choosing the motor is the most important component of our car's autonomous navigation system. The Lego MINDSTORMS EV3 kit includes two different motor options: large motors and medium motors. During the selection process, we considered key factors such as rotation speed, torque, and encoder accuracy. During [research](https://github.com/RobotekLumino/Future-Engineers-/tree/main/research/Motor_selection) on motor selection, we also added a large motor from the nxt kit.

![extract](./img/text.png)

The large motor provides considerable power, however, the medium motor, though less powerful, is smaller and lighter. The compact size provides faster responsiveness and saves space in the vehicle design.
Considering the limitations of our compact vehicle dimensions (300x200x300 mm) and the emphasis on high-speed navigation, we opted for the medium motor for both steering and driving mechanisms. Our car's drive system uses three Medium motors: one for steering and two for movement.

<p>The main body of the robot is assembled from LEGO construction elements. The robot has two different types of wheels: the front wheels are smaller than the rear ones. This decision was made to improve the robot's maneuverability and stability, as the smaller front wheels allow the robot to turn more easily and maintain balance while moving.</p>

<p>The robot is equipped with one medium motor located at the front, which controls the robot's forward movement and turning. To ensure power and direction of movement, two medium motors are used at the rear, which are connected to a differential. This allows the robot to have an efficient power transmission to both rear wheels, improving its stability and speed on straight sections of the path.</p>

### Key components of the control system:
- **One front medium motor** — controls forward movement and turning.
- **Two rear medium motors** — connected to a differential to provide power to both rear wheels.
- **LEGO construction elements** — used to assemble the robot's frame.
- **Differential** — distributes power between the rear wheels, improving grip and ensuring smooth movement.

  

## 3D Printing parts:

We used **Autodesk Fusion 360** to design components, and then printed these parts using PLA material with a 3D printer. This process allowed us to create accurate and individually tailored parts for our robot, ensuring optimal performance and compliance with design requirements. 3D files can be found at the following [link.](https://www.printables.com/model/164698-lego-technic-compatible-double-helical-gears)

### Double helical gears

As an important component for transmitting torque, we used **double helical gears**. These gears have several advantages over traditional ones: they have less backlash, which improves the accuracy of the mechanism. In addition, unlike single helical gears, double gears do not create lateral load on the shaft, which contributes to a more stable and durable gear train.

### Camera and mounting block
We developed a special [cover](models/pixy_2_cover.stl) and the [case](models/pixy_2_case.stl) for the camera. They were individually designed mounts for LEGO connectors. This unit not only securely holds the camera, but also provides its safe storage during transportation, preventing damage during robot movement.

## Steering mechanism with Ackermann angle
Our project uses a steering mechanism with Ackermann angle, which is important for ensuring efficient and precise control of the robot. While this principle generally minimizes tire wear and improves maneuverability, especially during turns, we used an approximated version of the Ackermann angle, assembled from LEGO construction elements.

#### Benefits of Ackermann angle:

The main advantage of [Ackermann angle](https://github.com/RobotekLumino/Future-Engineers-/tree/main/research/Ackermann_angle_study) is that it reduces tire slippage during turns, improving maneuverability. This is achieved by adjusting the steering mechanisms so that the inside wheel turns at a sharper angle than the outside one. Each wheel follows its own natural path during turns, leading to more precise steering and better control over the robot's movement.

In addition, this mechanism allows for a simpler steering system design, as it does not require complex gears, which reduces weight and the number of potential failure points. This simplified design also makes maintenance easier and reduces production costs.

#### How the Ackermann steering system works:

The principle of operation of the mechanism can be described as follows:

- **Transmitting the control signal:** When the motor is activated, the signal is transmitted through the steering levers to both front wheels. Specific angles and lengths of tie rods allow the inside wheel to turn at a sharper angle than the outside one.

- **Turns:** During a turn, the Ackermann geometry ensures that each wheel moves along its own path, minimizing slippage and improving grip.

#### Key system parameters:

- **Steering ratio:** In an Ackermann system, the steering ratio describes the ratio between the servo motor turning angle and the wheel turning angle. The higher this ratio, the less rotation of the servo motor is required for a greater turning angle of the wheels, which increases maneuverability.

- **Motor torque:** The torque of the medium motor depends on the force applied to the steering lever. This value affects steering resistance and robot movement stability.

- **Steering wheel turning angle:** The steering wheel turning angle determines how much the robot's direction of travel changes when the servo motor angle changes.




<img src="./img/akkerman.png" alt=".....">


## Our experience with Ackermann angle:

We started by using a steering mechanism with Ackermann angle, as it seemed like the optimal solution to improve the robot's maneuverability. However, after conducting a series of tests, we encountered some difficulties related to the accuracy and stability of the system.

- **Approximation issues:** Since the Ackermann angle was approximated and assembled from LEGO elements, the system had significant backlash, which negatively affected the accuracy of turns.
- **Unsatisfactory stability:** Despite the theoretical advantages of the Ackermann angle, in real conditions, our system without this mechanism proved to be more stable and reliable.

After numerous tests and experiments, we concluded that abandoning the full Ackermann angle improves the stability and reliability of our robot, and therefore decided to exclude it from the design.

### Final solution:

While the Ackermann angle has many advantages and was chosen by us at the initial stage of development, as a result of testing, we abandoned its use in full. This allowed us to achieve better stability and accuracy in the robot's movement. We decided to return to the parallel wheel connection.

<img src="./img/parallel.png" alt=".....">

## 2 - Differential gear

A **differential** is crucial for ensuring smooth and stable movement of a robot during turns. Without a differential, both of the robot's drive wheels rotate at the same speed, which makes turning difficult. This is because the inner wheel (relative to the center of the turn) travels a shorter distance than the outer wheel.

### Problems Without a Differential:
1. **Increased resistance**: The mismatch between wheel speeds leads to higher friction and reduced maneuvering efficiency.
2. **Jerks and skidding**: Unequal rotation can cause the wheels to slip, resulting in jerky movements and rapid wear of the tires.
3. **Reduced controllability**: Steering becomes less precise, especially during complex paths or tight maneuvers.


## How a Differential Works

A **differential** is a mechanism that allows drive wheels to rotate at different speeds while maintaining consistent torque distribution.

### Primary Functions of a Differential:
1. **Compensation for distance differences**: During a turn, the inner wheel travels a shorter path and must rotate slower than the outer wheel.
2. **Torque transfer**: The differential delivers driving force to both wheels, even if they spin at different speeds.
3. **Improved handling**: By synchronizing wheel speeds with the trajectory, the differential enables smooth and precise motion.


### How It Operates:
- The differential uses a **planetary gear system** to connect the drive shaft with both wheels.
- When moving straight, the gears rotate as a single unit, transmitting equal speed to both wheels.
- During a turn, the mechanism allows the inner wheel to slow down and the outer wheel to speed up. Torque is distributed proportionally to maintain stability and follow the desired path.


<strong>Gear ratio calculation:</strong>
<p>Before designing a differential gear, it is important to accurately calculate the gear ratio. To do this, it is necessary to take into account the motor characteristics and the design of the differential. The gear ratio can be calculated by counting the number of teeth on the gear housing and side gears:</p>

$$ \text{GR} = \frac{R}{S1 + S2} $$

<p>Where:</p>
<ul>
    <li><code>R</code> — number of teeth on the gear housing.</li>
    <li><code>S1</code> and <code>S2</code> — the number of teeth on each side gear.</li>
</ul>

<p>This ratio determines the distribution of torque and speed between the side gears of the differential. After calculating the gear ratio, you can establish the relationship between the motor speed and the wheel rotations. The wheel speed <sub>Н<sub>wheel</sub></sub> can be calculated using the formula:</p>

 $$ N_{\text{wheel}} = \frac{N_{\text{Motor, no-load}}}{\text{GR}} $$ 

<p>The wheel speed depends on the speed of the side gears of the differential, which directly affects the speed of the robot. Theoretical calculations provide approximate data, but in real conditions, calibration is necessary to take into account various limitations.</p>

### Weight Distribution

To improve grip and prevent wheel slippage on the rear axle, we specifically located the robot's center of gravity slightly closer to its middle. This helps achieve better stability and control, especially when moving at high speed. Proper weight distribution also contributes to smoother movement and reduces the likelihood of skidding, which in turn improves overall robot performance.

## Power and Sense Management

### Sensor Management

Our autonomous vehicle employs a combination of sensors to perform precise movements, which is crucial for both obstacle avoidance and qualifying trials in the competition.

Color Sensor: This sensor is used to determine turns and direction by reading colored lines (orange or blue) on the competition field. During the navigation phase, we use the color sensor to reset odometry by detecting two lines and applying mathematical formulas to reset the odometry.
[Color sensor selection](/research/Сolor_sensor_selection/README.md)

Ultrasonic Sensor: Positioned at the front of the vehicle, the ultrasonic sensor measures the distance between the vehicle and field barriers, ensuring that the vehicle's relative position before and after turns is consistently known.

Gyroscope Sensor: The gyroscope sensor plays a key role in maintaining proper alignment. It detects changes in the vehicle's angle of movement, alerting the system to any inaccuracies or deviations. The implementation of a PID (Proportional-Integral-Derivative) controller ensures that any deviation from the desired steering angle is continuously corrected, guaranteeing a straight and accurate trajectory.

The PID controller operates in a continuous cycle throughout the program, ensuring that the vehicle stays on its planned path, maintaining its autonomous navigation capabilities.

Pixy v2.1 Camera: The camera is used to detect and distinguish traffic signs and parking during a round

### Power Management
The power for the EV3 Brick and the whole vehicle comes from a rechargeable 10V Lithium Battery. Power management within the EV3 brick consists of multiple switching regulations which are tightly controlled and interlinked in order to boot the electronic circuit correctly.
To protect the EV3 brick from short circuit, 3 poly switches are included, one for each of the two motor drivers and one for the rest of the circuit. Each poly switch has a hold current at approximately 1.1 A and will be triggered at approximately 2.2 A.

### More details about each sensor and its power supply circuit can be found here:

[Color Sensor](/schemes/color-sensor/README.md)

[Gyro Sensor](/schemes/gyro-sensor/README.md)

[Medium Motor](/schemes/medium-motor/README.md)

[Pixy v2](/schemes/pixy2_camera/README.md)

[Ultrasonic Sensor](/schemes/ultrasonic-sensor/README.md)

[EV3 P-Brick](/schemes/programmable-brick/README.md)

[Rechargeable Battery](/schemes/Internal_battery_components/README.md)


### Obstacle Management

Effective obstacle management is a critical aspect of our autonomous self-driving robot's navigation system, ensuring it can safely and intelligently navigate through challenging scenarios in the WRO competition. In this section, we elaborate on our obstacle management strategies and the key components involved in this crucial aspect of our robot's functionality.

### Coordinate system and robot position correction

In our approach to solving the **Open Challenge**, we construct a coordinate system where 0 is the center of the field, and 50 and -50 are the coordinates of the track walls. This system allows the robot to accurately navigate in space and avoid collisions with the track boundaries.

As the robot moves along the track, its position is constantly monitored, and if the deviation value from the center exceeds 45 (for example, the robot approaches the wall at a distance of less than 5 units), the system automatically performs correction, returning the robot to the center. This is important for maintaining a stable trajectory and preventing the robot from entering dangerous areas.

Thus, the coordinate system works as follows:

- **0** — the center of the field, the reference point.
- **50 and -50** — the coordinates of the track walls, the boundaries that the robot should not cross.
- If the deviation from the center of the field becomes greater than 45, the system automatically adjusts the robot's movement, returning it to a safe zone where it can move with minimal collision risks.

This approach allows you to effectively control the robot's movement, ensuring its safe passage along the track and preventing unwanted collisions.

<img src="./img/algorithm-center.png" alt="Algorithm Center" style="max-width: 500px; height: auto; display: block; margin: 0 auto;">

### Turn detection and direction control

The robot turns immediately after detecting a line. After each turn, the gyroscope data is reset, which helps to reduce the number of incorrect turns and improve navigation accuracy. The direction of the turn (clockwise or counterclockwise) is determined based on what the first line was at the start.

This algorithm allows the robot to move efficiently and accurately along the track, coping with turns and different areas, which contributes to achieving better lap times.


<hr>

# Computer Vision
   


Computer vision is a key technology in robotics, playing a crucial role in the perception and interpretation of the environment by unmanned vehicles. In our project, computer vision methods help the robot collect important information necessary for decision making and performing actions such as object recognition and collision avoidance.

To detect objects, including pink parking zones and red/green posts, we use **Pixy v2.1**, a powerful and affordable computer vision sensor. Pixy v2.1 is equipped with a built-in camera and processor that enable real-time object recognition. This sensor is ideal for autonomous robot navigation and collision avoidance.

We configure Pixy v2.1 using **PixyMon v2**, special software for configuring the camera and setting parameters for various objects such as color tags (parking zones, poles, etc.). Pixy v2.1 uses computer vision algorithms to process images and recognize objects, allowing the robot to accurately navigate in space and avoid collisions with surrounding objects.

### 1 - Camera position

The camera is mounted on a high position at the rear of the robot, which provides a wide view and helps to more accurately control obstacles in the path. In order for the camera to effectively track objects located near the robot, it is tilted slightly downwards. This allows limiting the viewing range, but improves the perception of nearby objects and obstacles, ensuring more accurate control over the situation around the robot.


**Pixy2.1** — is a camera that is designed for use in robotics. Some key features of Pixy 2.1:

- **Camera resolution:** 640x400 pixels.
- **Color recognition:** Support for color filters (RGB, HSV) for accurate object identification.
- **Image processing algorithms:** Built-in image processing for fast object recognition.
- **Communication:** Connection via USB, SPI, I2C interfaces, as well as the ability to connect via UART.
- **Speed of operation:** The camera response time is up to 60 frames per second, which allows using Pixy2 for fast and accurate data processing.

Pixy2 provides high accuracy and reliability when operating in real-time, making it an ideal choice for robots that need to recognize objects and avoid collisions.

 <div align="center">
<img src="./schemes/img/Pixy2.1.png" width="400" height="400">
<p>Pixy v2.1 Camera </p>
</div>

### 2 - Image processing with Pixy2.1

#### Setting camera parameters

To configure the **Pixy2.1** camera, we use its built-in capabilities for adapting to different lighting conditions. Depending on the ambient lighting level, the Pixy2.1 camera can automatically or manually adjust shooting parameters for optimal image capture. In bright conditions, the camera sensor limits exposure to prevent overload, while in low light conditions, it increases exposure, allowing more light to be captured for accurate operation.

#### Image pre-processing

Image pre-processing is important for correct object recognition, such as parking zones and poles. At this stage, noise filtering and image cleaning occur, which can interfere with accurate object identification. Pixy2.1 processes images using built-in algorithms to improve quality and accuracy of analysis. This includes removing unnecessary fragments that may be misinterpreted as target objects, and cropping the frame area to focus on key elements.

#### Masking

To isolate certain colors in the image, the **Pixy2.1** camera uses the HSV color space. In the masking process, the image is converted from the BGR color space to HSV, where the desired color range is selected (red, green, pink). Each pixel of the image is analyzed to determine if it falls within the specified range of shades. If the pixel falls within this range, it becomes white on the mask, otherwise — black. The resulting mask helps to accurately highlight areas with the desired color, which is critical for object recognition.

#### Benefits of using Pixy2.1

- **Color tuning and filtering:** Pixy2.1 supports precise color tuning and filtering using the HSV space, which allows it to work effectively in different lighting conditions.
- **High-speed processing:** The Pixy2.1 camera processes the image in real time at a high frame rate, ensuring a quick robot response to environmental changes.
- **Automatic object recognition:** Pixy2.1 uses algorithms to recognize predefined objects, allowing the robot to identify obstacles and navigate around them to perform tasks.

Configuring Pixy2.1 is done through **PixyMon v2**, which allows you to flexibly adjust parameters for different objects and conditions.

<div align="center">
<img src="./img/pixymon.png" width="800" height="500">
<p>PixyMon v2 interface</p>
</div>

### Trajectory Calibration

Calibrating the robot's trajectory is a vital step in ensuring it safely navigates around obstacles. This process involves placing obstacles in designated locations on the competition field and guiding the robot to drive around them. As the robot maneuvers around obstacles, we record the coordinates of these obstacles in a table for later analysis and fine-tuning.
Once the obstacle coordinates are collected, we import this data into software tools such as Microsoft Excel or Google Sheets. In these programs, we create graphical representations, which often take the form of exponential functions. This function encapsulates the ideal path for the robot to follow when circumventing obstacles.

<img src="./img/graph.jpeg" alt="...">


### Autonomous Robot Navigation

Our robot's program integrates an optimized obstacle avoidance trajectory. The system employs a regulator to analyze and process trajectory data in real-time. This regulator continuously monitors the robot’s position relative to obstacles and adjusts its path to ensure smooth and efficient navigation. A PID (Proportional-Integral-Derivative) controller is used for precise tuning and enhancing the robot's responsiveness during obstacle avoidance.

## Parking Algorithm

### Completion of the Main Route
After completing three laps along the route, the robot determines the direction in which the ultrasonic sensor is pointing.

### Turning towards the outer wall
If by the time the laps are completed, the ultrasonic sensor is pointing inwards, the robot turns so that the sensor is oriented towards the outer wall.

### Moving along the outer wall
After turning, the robot aligns itself along the outer wall and begins to move parallel to it, maintaining the optimal distance for searching for a parking space.

### Finding a parking space using the Pixy camera
While moving along the wall, the robot uses the Pixy camera to search for a parking space. The camera is configured to recognize the color markings indicating the parking zone, which allows the robot to stop at the desired point in time.

### Parking maneuver
After detecting the parking zone, the camera sends a signal to the robot, which then performs the parking maneuver, carefully driving into the designated space.
<br>

<img src="./img/parking.png" width="400" height="400">

## Problems when preparing for competitions

#### 1. Low odometry accuracy

Odometry, used to determine the distance traveled and the angle of rotation based on wheel rotation data, proved to be one of the key problems. The system often showed large errors, which negatively affected the accuracy of movement and robot orientation. The main reasons for inaccuracy were as follows:

- **Error accumulation:** Any, even the slightest wheel slippage or inaccuracy in measuring turning angles led to error accumulation in the data. This made the robot's trajectory less predictable, especially over long distances.
- **Lack of sensors for correction:** With a limited number of ports on the EV3, it was impossible to connect additional sensors to reset odometry accurately enough. This created difficulties in accurately resetting values and complicated the assessment of the robot's current position.

Because of this, we decided to abandon odometry in favor of a more reliable algorithm.

#### 2. Limited number of ports on EV3

The EV3 Mindstorms system has only four ports for sensors, which made it difficult to optimally distribute the sensors for effective performance of all tasks. We had a set of sensors that need to be included in the robot for Open and Obstacle Challenge rounds. 

- **Gyroscope for stabilization:** The gyroscopic sensor ensured accuracy in turns and prevented unwanted deviations.
- **Color sensor for line detection:** This sensor was used to track the line to determine turns and the direction of the round at the start.
- **Camera for object recognition:** The camera provided recognition of road signs and parking.

Due to the limited number of ports, we had to leave only one ultrasonic sensor. This made it difficult to control obstacles, as one ultrasonic sensor did not allow for effective tracking of the walls on both sides of the robot.

#### 3. Problems with transmitting data from the color sensor in RGB mode
   When using the color sensor in RGB mode, the robot tried to transmit data from this sensor to the computer via Bluetooth. However, due to the lack of support for this mode in the default Mindstorms firmware, the system could not transmit data, and the sensor periodically rebooted. The solution to this problem is to not use Bluetooth to operate the robot and upload the program via a cable. This avoided reboots, but at the same time limited us in the ability to receive sensor and encoder data during the robot's race.


#### 4. Problems with the Ackermann steering mechanism

We started by using a steering mechanism with Ackermann angle, as it seemed like the optimal solution to improve the robot's maneuverability. However, after conducting a series of tests, we encountered some difficulties related to the accuracy and stability of the system.

- **Approximation issues:** Since the Ackermann angle was approximated and assembled from LEGO elements, the system had significant backlash, which negatively affected the accuracy of turns.
- **Unsatisfactory stability:** Despite the theoretical advantages of the Ackermann angle, in real conditions, our system without this mechanism proved to be more stable and reliable.

After numerous tests and experiments, we concluded that abandoning the full Ackermann angle improves the stability and reliability of our robot, and therefore decided to exclude it from the design.

## Photos

### Vehicle Photos

![Robot](./img/Betman.png)

<div align="center">
  <table>
    <tr align="center">
      <td><img src="./img/top.png" alt="Robot Photo 1" width="60%"></td>
      <td><img src="./img/back.png" alt="Robot Photo 2" width="80%"></td>
      <td><img src="./img/bottom.png" alt="Robot Photo 3" width="90%"></td>
    </tr>
    <tr align="center">
      <td><img src="./img/right.png" alt="Robot Photo 4" width="70%"></td>
      <td><img src="./img/front.png" alt="Robot Photo 5" width="70%"></td>
      <td><img src="./img/left.png" alt="Robot Photo 6" width="70%"></td>
    </tr>
  </table>
</div>

  <li>You can see a photo of the robot <a href="https://github.com/RobotekLumino/Future-Engineers-/tree/main/v-photos" target="_blank">here</a></li>

### Team Photos

![teamph2](./t-photos/t1.jpg)
![teamph](./t-photos/t2.jpg)

***

## Performance Videos

Qualification Round Challenge: [https://youtu.be/6GB2IOQi8mM?si=YZQlWzMltXwP1cnq](https://youtu.be/6GB2IOQi8mM?si=YZQlWzMltXwP1cnq)

Obstacle Round Challenge: [https://youtu.be/r2_ArxA0ATI?si=F9Ab_i3WUzBK2m0p](https://youtu.be/r2_ArxA0ATI?si=F9Ab_i3WUzBK2m0p)

Robot parts discussion: [https://youtu.be/gbITDXvny-k](https://youtu.be/gbITDXvny-k)

***

## Conclusion

### Limitations of our platform

Our project encountered a number of limitations associated with using LEGO EV3, which affected the overall efficiency and flexibility of the system.

**Mobility Management:**
- LEGO motors, sensors, and P-Brick are large in size compared to other platforms where motors have more power with more compact sizes.
- The LEGO EV3 kit has limited capabilities for creating Ackermann steering geometry, which complicates the development process and movement control.
- Creating a design exclusively using LEGO makes the robot less compact and limits opportunities for space optimization.

**Power and Sense Management:**
- The single-core processor deprives the system of multitasking capabilities, which reduces the accuracy of processing data and sensor readings.
- The platform is limited to four ports for connecting sensors and four ports for motors, which limits the possibilities for connecting additional sensors and components.
- The EV3 P-Brick operating system has limited functionality and flexibility, hindering the implementation of more complex algorithms and integrations.
- The EV3 P-Brick is limited in motor and sensor sources, as special firmware is required to work with them, which complicates further development.
- The EV3 platform is not updated and has some bugs, such as active Bluetooth mode, which sometimes interferes with the normal operation of sensors.
- LEGO sensors have less accuracy compared to other available analogues.

**Obstacle Management:**
- The Pixy2 camera has a low resolution (1.3 megapixels), which limits its ability to detect objects at a long distance.
- Using I2C for data transmission limits the refresh rate to 60 readings per second, which reduces the speed of information processing.
- The camera outputs only predefined data, which limits its flexibility in various scenarios.
- The camera is highly dependent on the level of illumination, which reduces its accuracy and reliability in variable lighting conditions.

---

### Suggestions for Further Development

To overcome the existing limitations, we propose considering several options for expanding capabilities and improving system performance.

1. **Expanding the number of ports**:
   One possible solution is to connect the EV3 block to Arduino to increase the number of ports, which will allow connecting additional sensors and components. However, this solution has its drawbacks:
   - **Slow data transfer**: Data transfer between EV3 and Arduino will be less fast and efficient compared to using a single platform.
   - **Integration complexity**: Connecting two platforms requires the development and configuration of additional interfaces and software, which increases the complexity of the project.
   - **Power limitations**: Arduino cannot provide the same computing power as more modern platforms, which also affects performance.

2. **Transition to a more powerful platform, such as Raspberry Pi 5**:
   Currently, one of the most promising alternatives is to transition to the Raspberry Pi 5 platform. Switching to this platform will open up new opportunities to improve system performance:
   - **Multitasking**: Raspberry Pi 5 supports multitasking, allowing simultaneous data processing from multiple sensors and running complex algorithms.
   - **High computing power**: Raspberry Pi 5 is equipped with a multi-core processor with high performance, which will allow you to efficiently process video and images, as well as use complex algorithms to build maps and avoid obstacles.
   - **Flexibility and expandability**: Raspberry Pi 5 has many ports and supports a wide range of connectable devices, significantly increasing the possibilities for further modification and expansion.
   - **Support for modern sensors**: Raspberry Pi 5 can easily integrate more accurate and high-speed sensors, which will improve the accuracy and speed of the system.
   - **Support for AI for obstacle avoidance**: The Raspberry Pi 5 platform provides the ability to use artificial intelligence (AI) algorithms for smarter obstacle avoidance, building a map of the area, and optimizing the route, which will significantly improve the robot's autonomy.

Switching to the Raspberry Pi 5 platform will not only solve current problems with port and computing power limitations, but also provide significantly more flexibility in development, adding new features and increasing the accuracy of the robot's operation.

  <h2>References</h2>
<ul>
  <li>LEGO Mindstorms EV3 Documentation. <a href="https://makecode.mindstorms.com/docs" target="_blank">Link</a></li>
  <li>Pixy2 Camera Documentation. <a href="https://pixycam.com/category/pixy/" target="_blank">Link</a></li>
  <li>LEGO Mindstorms EV3: Understanding and Using the Motors. <a href="https://ev3-help-online.api.education.lego.com/Education/en-gb/page.html?Path=editor%2FUsingSensors_MotorRotation.html" target="_blank">Link</a></li>
  <li>Understanding Ackermann Steering Geometry. <a href="https://en.wikipedia.org/wiki/Ackermann_steering_geometry" target="_blank">Link</a></li>
  <li>Odometry in Robotics. <a href="https://robocraft.ru/technology/736" target="_blank">Link</a></li>
  <li>Guide to creating your own custom blocks. <a href="http://www.proghouse.ru/article-box/106-ev3-block" target="_blank">Link</a></li>
</ul>
