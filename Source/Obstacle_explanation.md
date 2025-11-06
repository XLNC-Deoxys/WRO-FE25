# Obstacle Navigation Program (`Obstacle.bp`)

This file implements the complete autonomous navigation logic for the **XLNC Deoxys** robot during the WRO Future Engineers 2025 obstacle challenge. It integrates real-time data from multiple sensors—**gyro**, **color**, **ultrasonic**, and **Pixy2 camera**—and runs concurrent threads to manage steering, perception, and visual feedback.

[Full source code →](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Obstacle.bp)

---

## 1. Importing Modules and Sensor Setup

```vb
import "Mods\AdvEncoder"
import "Mods\AdvGyro"
import "Mods\ColorRGB"
import "Mods\SteerControl"
import "Mods\AdvUltrasonic"
import "Mods\Tool"
import "Mods\AdvPixy"
```

These imports load custom libraries for enhanced EV3 functionality: encoder precision, gyro calibration, RGB normalization, ultrasonic readings, and Pixy2 vision.

```vb
Sensor.SetMode(1, 0)
Sensor.SetMode(2, 4)
Sensor.SetMode(3, 0)
Sensor.SetMode(4, 0)
```

Configures all sensors. Ports 1–4 correspond to ultrasonic, color, gyro, and other modules.

---

## 2. Gyro Reset Procedure

```vb
AdvGyro.CheckReset(3, result)
While result = 0
  Program.Delay(1000)
  AdvGyro.HardReset(3)
  AdvGyro.CheckReset(3, result)
EndWhile
```

This loop ensures a clean reset of the gyro sensor. The robot waits until the gyro confirms readiness before proceeding, guaranteeing angle accuracy.

---

## 3. Color Sensor Configuration

```vb
col = EV3File.OpenRead("col")
Rmin = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Rmax = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Gmin = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Gmax = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Bmin = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Bmax = EV3File.ConvertToNumber(EV3File.ReadLine(col))
ColorRGB.Config(Rmin, Rmax, Gmin, Gmax, Bmin, Bmax)
```

Reads calibration parameters from file `col`. This enables consistent color detection (white/orange) across different lighting environments.

---

## 4. Steering and Encoder Initialization

```vb
AdvGyro.ResetPort3(0)
AdvEncoder.Config()
SteerControl.Config(1.5, 0.05, 3, 35, 88)
```

* Gyro reset to 0°.
* Encoders configured.
* PID steering control gains tuned for balanced performance.

```vb
MotorA.StartPower(-80)
Program.Delay(2000)
MotorA.ResetCount()
```

Pushes steering motor A to its limit, sets that as the zero reference, ensuring alignment calibration.

---

## 5. Variable Declarations

```vb
angleKp = 0.8
angleKd = 1.2
angleOld = 0
clockWise = 0
turnCounter = 0
turnAngle = 91
UArtReady = 0
I2CReady = 0
SteeringReady = 0
DisplayReady = 0
aimx=30
distance=2000
yCameraRange=20
```

Defines PID gains, turning direction flags, synchronization flags for threads, and initial target variables.

---

## 6. Multithreading Structure

### UART Thread

```vb
Sub UArt
  UArtReady = 1
  While 1=1
    AdvGyro.WritePort3(gyroAngle)
    ColorRGB.ReadPort2(r, g, b)
    AdvUltrasonic.ReadPort1(Distance)
  EndWhile
EndSub
```

Constantly updates gyro angle, RGB values, and distance measurements for real-time feedback.

### I2C Thread

```vb
Sub I2C
  I2CReady = 1
  While 1=1
    AdvPixy.getLargest(4, pixyX, pixyY, signature)
  EndWhile
EndSub
```

Retrieves object coordinates (X/Y) and color signature from Pixy2 camera. Used for object avoidance and centering.

### Steering Thread

```vb
Sub Steering
  SteeringReady = 1
  While 1=1
    SteerControl.Core(MotorA.GetTacho(), powerC)
    MotorA.StartPower(powerC)
  EndWhile
EndSub
```

Runs continuously to keep steering power balanced using encoder feedback and PID output.

### Display Thread

```vb
Sub Display
  DisplayReady = 1
  While 1=1
    If @Distance >= 100 Then
      @Distance = 0
    EndIf
    count = @Distance / 10
    Txt = ""
    While count > 0
      Txt = Text.Append(Txt, "@")
      count -= 1
    EndWhile
    LCD.Text(1, 10, 10, 2, Txt)
    Program.Delay(25)
    LCD.Clear()
  EndWhile
EndSub
```

Shows live ultrasonic data on the EV3 display using a bar graph made of '@'.

---

## 7. Core Functions

### ColorCheck()

Checks RGB readings to identify white floor and orange markers:

```vb
If @b < 55 Then isWhite=0 Else isWhite=1
If @r > 85 Then isOrange=1 Else isOrange=0
```

### AngleCore()

Implements a proportional-derivative correction for steering control:

```vb
aim = @angleKp * angle + @angleKd * (angle - @angleOld)
```

Stores last angle for derivative term.

### Reset()

Resets gyro reference after each turn and increments counter:

```vb
If @clockWise = 0 Then AdvGyro.ResetPort3(@gyroAngle + turnAngle)
Else AdvGyro.ResetPort3(@gyroAngle - turnAngle)
@turnCounter++
Speaker.Tone(100,300,50)
Time.Reset1()
```

### DetourObstacle()

Handles obstacle avoidance using Pixy2 data:

```vb
If @signature = 2 Then
  desiredX = -0.0025*@pixyY*@pixyY + 0.8*@pixyY + 35
Else
desiredX = 0.0025*@pixyY*@pixyY - 0.8*@pixyY - 35
SteerControl.SetTarget((desiredX - @pixyX) * 1)
```

Switches LED colors to visualize avoidance direction.

### Autopilot()

Controls whether the robot continues straight or detours:

```vb
If @signature=0 Or @Distance>75 Or @Distance<15 Then
  Center()
Else
  MotorB.SetPower(100)
  DetourObstacle()
EndIf
```

Ensures dynamic transitions between line-following and obstacle-avoidance.

### Center()

Centers the robot between obstacles using gyro and distance sensors:

```vb
dist = 44 - Math.Cos(Math.GetRadians(@gyroAngle * 1.3)) * dist
Tool.constrain(dist,-25,25,U)
AngleCore((@gyroAngle+U) * 2.5,aim)
SteerControl.SetTarget(aim)
```

### GetOutOfParking()

Executes initial reverse-turn maneuver:

```vb
MotorB.StartPower(-35)
While @gyroAngle > -30
  SteerControl.SetTarget(-45)
EndWhile
```

Completes alignment and resets encoder.

---

## 8. Main Control Flow

### Thread Start and Synchronization

```vb
Thread.Run = UArt
Thread.Run = I2C
Thread.Run = Steering
Thread.Run = Display
While UArtReady=0 Or SteeringReady=0 Or I2CReady=0 Or DisplayReady=0
EndWhile
```

All sensor and control threads initialize before the mission begins.

### Start()

```vb
MotorB.StartPower(60)
While isWhite=1
  Autopilot(1)
  ColorCheck(isWhite, isOrange)
EndWhile
@clockwise=isOrange
Speaker.Tone(50,3000,100)
Reset(@turnAngle)
```

Drives forward until the orange marker is detected; defines turning direction (clockwise or counterclockwise).

### Main Navigation Loop

```vb
While turnCounter<12
  isWhite=1
  isOrange=0
  While @clockWise<>isOrange Or isWhite=1 Or Time.Get1()<1000
    Autopilot(0)
    ColorCheck(isWhite, isOrange)
  EndWhile
  Speaker.Tone(50,3000,100)
  Reset(turnAngle)
EndWhile
```

Repeats 12 checkpoint segments; adjusts steering and executes turns based on color detection.

---

## 9. Final Stage: Return and Finish

After all checkpoints:

```vb
MotorB.ResetCount()
While MotorB.GetTacho()<3000
  Center()
EndWhile
MotorB.OffAndBrake()
Program.Delay(5000)
```

Drives back to start line and pauses.

### Final Turns and Alignment

Performs complex rotations to finish precisely:

```vb
While @gyroAngle < 90
  SteerControl.SetTarget(-35)
EndWhile
MotorB.SetPower(-40)
```

Then executes backward and forward alignment until reaching 175°, signaling end of course.

---

## 10. Finish Sequence

```vb
MotorB.OffAndBrake()
Speaker.Tone(100,3000,300)
Speaker.Wait()
Speaker.Tone(100,3000,300)
Speaker.Wait()
Speaker.Tone(100,3000,300)
Speaker.Wait()
```

Three tones confirm mission success and termination.

---

## Summary

* **Threads:** manage sensor reading, vision, steering, and display concurrently.
* **Functions:** implement adaptive PD control for navigation and obstacle avoidance.
* **Flow:** starts from parking, completes 12 turns, avoids obstacles, and returns to start.

[Full source code link](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Obstacle.bp)
