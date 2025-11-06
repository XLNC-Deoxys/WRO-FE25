# Open Navigation Program (`Open.bp`)

This program controls the **XLNC Deoxys** robot during the *Open Track* stage of the WRO Future Engineers 2025 challenge. It handles autonomous line following, color detection, and steering correction based on dual ultrasonic sensors. The system runs multithreaded routines for real-time control and display feedback.

[Full source code →](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Open.bp)

---

## 1. Imports and Sensor Setup

```vb
import "Mods\AdvEncoder"
import "Mods\AdvGyro"
import "Mods\ColorRGB"
import "Mods\SteerControl"
import "Mods\AdvUltrasonic"
import "Mods\Tool"
```

Custom libraries extend basic EV3 functionality:

* **AdvGyro** – gyro reset and angle tracking.
* **ColorRGB** – RGB calibration for color detection.
* **SteerControl** – PID steering management.
* **AdvUltrasonic** – dual ultrasonic distance reading.
* **Tool** – mathematical and selection utilities.

```vb
Sensor.SetMode(1, 0)
Sensor.SetMode(2, 4)
Sensor.SetMode(3, 0)
Sensor.SetMode(4, 0)
```

Initializes sensor modes: ultrasonic, color, gyro, and auxiliary sensors.

---

## 2. Gyro and Color Sensor Initialization

```vb
AdvGyro.CheckReset(3, result)
While result = 0
  Program.Delay(1000)
  AdvGyro.HardReset(3)
  AdvGyro.CheckReset(3, result)
EndWhile
```

Ensures the gyro sensor is properly reset before movement.

```vb
col = EV3File.OpenRead("col")
Rmin = EV3File.ConvertToNumber(EV3File.ReadLine(col))
...
Bmax = EV3File.ConvertToNumber(EV3File.ReadLine(col))
ColorRGB.Config(Rmin, Rmax, Gmin, Gmax, Bmin, Bmax)
```

Loads color calibration parameters from file `col`, ensuring stable white/orange recognition across lighting conditions.

---

## 3. Steering Configuration and Calibration

```vb
AdvGyro.ResetPort3(0)
AdvEncoder.Config()
SteerControl.Config(1.5, 0.05, 3, 40, 88)
```

Sets up gyro, encoder, and PID constants for steering stability.

```vb
MotorA.StartPower(-80)
Program.Delay(2000)
MotorA.ResetCount()
```

Moves the steering motor to its physical limit to calibrate the encoder at zero.

---

## 4. Variable Initialization

```vb
angleKp = 0.8
angleKd = 1.2
angleOld = 0
clockWise = 0
turnCounter = 0
turnAngle = 92
UArtReady = 0
SteeringReady = 0
DisplayReady = 0
```

Defines control gains, turning direction, counters, and synchronization flags for multithreading.

---

## 5. Multithreaded Subsystems

### UART Thread

```vb
Sub UArt
  UArtReady = 1
  While 1=1
    AdvGyro.WritePort3(gyroAngle)
    ColorRGB.ReadPort2(r, g, b)
    AdvUltrasonic.ReadPort1(RDistance)
    AdvUltrasonic.ReadPort4(LDistance)
  EndWhile
EndSub
```

Continuously updates gyro angle, RGB values, and left/right ultrasonic distances for navigation control.

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

Executes PID-based steering correction in a constant loop.

### Display Thread

```vb
Sub Display
  DisplayReady = 1
  While 1=1
    LCD.Text(1, 10, 10, 2, r)
    LCD.Text(1, 10, 40, 2, g)
    LCD.Text(1, 10, 70, 2, b)
    LCD.Text(1, 10, 100, 2, isWhite)
    Program.Delay(25)
    LCD.Clear()
  EndWhile
EndSub
```

Displays live color sensor values and white detection state on the EV3 LCD.

---

## 6. Core Functions

### ColorCheck()

```vb
If @b < 50 Then isWhite = 0 Else isWhite = 1
If @r > 85 Then isOrange = 1 Else isOrange = 0
```

Checks the RGB readings to identify white surface or orange checkpoint.

### AngleCore()

```vb
aim = @angleKp * angle + @angleKd * (angle - @angleOld)
```

Computes PD control output for angle correction.

### Reset()

```vb
If @clockWise = 0 Then AdvGyro.ResetPort3(@gyroAngle + turnAngle)
Else AdvGyro.ResetPort3(@gyroAngle - turnAngle)
@turnCounter++
Time.Reset1()
```

Resets gyro reference after each checkpoint and increases the turn counter.

### Center()

```vb
Tool.select(@clockwise, @LDistance, @RDistance, Distance)
If Distance > 100 Then Distance = 0
Distance = Math.Cos(Math.GetRadians(@gyroAngle * 1.3)) * Distance
Tool.select(@clockwise, Distance - @aimx, @aimx - Distance, Distance)
Tool.constrain(Distance, -25, 25, U)
AngleCore((@gyroAngle + U) * 2, aim)
SteerControl.SetTarget(aim)
```

Keeps the robot centered between left and right walls using dual ultrasonic sensors and gyro correction.

---

## 7. Start Sequence

```vb
MotorB.StartPower(50)
While isWhite = 1 Or Time.Get1() < 1000
  AngleCore(@gyroAngle, angle)
  SteerControl.SetTarget(angle)
  ColorCheck(isWhite, isOrange)
EndWhile
@clockwise = isOrange
Speaker.Tone(50, 3000, 100)
```

Robot starts driving until the orange marker is detected. The marker color defines the initial turning direction.

Next, it calculates distance to the nearest wall using ultrasonic sensors:

```vb
Tool.select(@clockwise, @LDistance, @RDistance, Distance)
If Distance >= 50 Then arriv = 500
ElseIf Distance >= 39 Then arriv = 250
Else arriv = 90
EndIf
```

Then moves forward to reach the appropriate lane distance before executing the first turn:

```vb
MotorB.ResetCount()
While MotorB.GetTacho() < arriv
  Center()
EndWhile
Reset(@turnAngle)
```

---

## 8. Main Loop

```vb
Thread.Run = UArt
Thread.Run = Steering
Thread.Run = Display
While UArtReady = 0 Or SteeringReady = 0 Or DisplayReady = 0
EndWhile
Start()
MotorB.StartPower(100)
```

All subsystems run concurrently. The robot then begins continuous autonomous driving.

```vb
While turnCounter < 12
  isWhite = 1
  isOrange = 0
  While @clockWise <> isOrange Or isWhite = 1 Or Time.Get1() < 2000
    Center()
    ColorCheck(isWhite, isOrange)
  EndWhile
  MotorB.ResetCount()
  While MotorB.GetTacho() < 1000
    Center()
  EndWhile
  Speaker.Tone(50, 3000, 100)
  Reset(turnAngle)
  Time.Reset1()
EndWhile
```

This loop executes **12 turn cycles**. Each cycle performs line following and precise turning when an orange marker is detected.

---

## 9. Finish Routine

```vb
MotorB.ResetCount()
While MotorB.GetTacho() < 4000
  Center()
EndWhile
MotorB.OffAndBrake()
```

Robot drives back toward the start line, maintaining central alignment.

Finally, the robot plays a triple tone signal indicating completion:

```vb
Speaker.Tone(100, 3000, 300)
Speaker.Wait()
Speaker.Tone(100, 3000, 300)
Speaker.Wait()
Speaker.Tone(100, 3000, 300)
Speaker.Wait()
```

---

## Summary

* **Threads:** manage gyro, ultrasonic, and steering feedback.
* **Functions:** provide modular control for color detection, centering, and turning.
* **Goal:** follow an open track autonomously through 12 segments with precise centering and PD-based steering.

[Full source code →](https://github.com/XLNC-Deoxys/WRO-FE25/blob/main/Source/Open.bp)
