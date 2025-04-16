On May 5, we collected data for a graph of error versus angle and studied the conversion from polar to Cartesian coordinates and vice versa, odometry, tactics for zeroing odometry, and determining the position of bars.

<h1> Research: </h1>

Last year, we reset the robot's position on turns. But if the robot was at an angle, the ultrasonic sensor showed incorrect data. To find the real distance from the robot to the wall, we decided to make a graph of error versus angle. Error refers to the difference between what the sensor outputs and the expected data. We expected that the graph would not depend on the distance from the robot to the wall. We tried to collect this data on April 30, but the distances turned out to be very inaccurate because we measured them with a ruler.
<div align=center>

 <img src="../Images/README_photos/Explanatory_board.jpg" height="400">
 <img src="../Images/README_photos/Explanation.jpg" height="500">
</div>
<div align=center>
 
 1st test’s error graph at a distance of 10 cm:
 
 <img src="../Images/README_photos/Test1Graph1.png" height="300">
 
 1st test’s error graph at a distance of 25 cm:
 
 <img src="../Images/README_photos/Test1Graph2.png" height="300">
 
 1st test’s error graph at a distance of 50 cm:
 
 <img src="../Images/README_photos/Test1Graph3.png" height="300">
 
 1st test’s error graph at a distance of 100 cm:
 
 <img src="../Images/README_photos/Test1Graph4.png" height="300">
</div>
The graphs are similar at distances of 50 and 100 cm.

<h2> 2nd test: </h2>

On May 5, we needed to collect data again, but this time more accurate.

<h3> Plan: </h3>

*	Make a measuring robot. Need ultrasonic sensor, gyroscope, EV3 Brick.	The ultrasonic sensor must be placed on a rotating platform with a gyroscope.

*	Write code:	Write data to a file at the click of a button.

* Take measurements:	Smoothly rotate the platform by pressing the button.	Once the ultrasonic sensor starts showing 255, you need to change the distance.

*	Transfer data from file to table

# [Code:](https://github.com/RobotekPRIME2024/WRO-FE24/blob/main/Ultrasonic_research/Test2Code.ev3)

<div align=center>

 <img src="../Images/README_photos/Program_for_measurements.png">
</div>
Measuring process (robot without wheels):
<div align=center>

 <img src="../Images/README_photos/Measurement.jpg" height="500">
</div>
Final robot for measurements:
<div align=center>

 <img src="../Images/README_photos/Robot_for_measuring.jpg" height="600">
</div>
As a result of the 2nd tests, we got this graph:
<div align=center>

 <img src="../Images/README_photos/Test2Graph1.png" height="500">
</div>
<h2> Conclusions: </h2>
The graph of error versus angle can be roughly expressed by the function 
y=0.00856x^2-0.0967x+0.345

error=0.00856angle^2-0.0967angle+0.345

error=horisontal_dist/cos(angle*π/180)
<div align=center>
 
 2nd test’s error graph at a distance of 9.1 cm:

 <img src="../Images/README_photos/Test2Graph2.png" height="300">

 2nd test’s error graph at a distance of 17.9 cm:

 <img src="../Images/README_photos/Test2Graph3.png" height="300">

 2nd test’s error graph at a distance of 25.5 cm:

 <img src="../Images/README_photos/Test2Graph4.png" height="300">
 
 2nd test’s error graph at a distance of 33.8 cm:

 <img src="../Images/README_photos/Test2Graph5.png" height="300">

 2nd test’s error graph at a distance of 42 cm:

 <img src="../Images/README_photos/Test2Graph6.png" height="300">

 2nd test’s error graph at a distance of 50 cm:

 <img src="../Images/README_photos/Test2Graph7.png" height="300">

 2nd test’s error graph at a distance of 59 cm:

 <img src="../Images/README_photos/Test2Graph8.png" height="300">

 2nd test’s error graph at a distance of 67 cm:

 <img src="../Images/README_photos/Test2Graph9.png" height="300">
 
 2nd test’s error graph at a distance of 75 cm:

 <img src="../Images/README_photos/Test2Graph10.png" height="300">

 2nd test’s error graph at a distance of 82.6 cm:

 <img src="../Images/README_photos/Test2Graph11.png" height="300">
</div>
<h2> The final results of the research: </h2>

<img src="../Images/README_photos/Test2Graph12.png">
length - angle, width - distance, height - error.

We will take this into account when measuring the distance from the robot to the wall, to minimize the difference between what the sensor produces and the expected data. Thanks to this, our robot will more accurately determine its distance to the wall, which will make his drive more stable.
