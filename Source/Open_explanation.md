# `Open2.bp` program explanation

This document explains the full logic and structure of the `Open2.bp` program used in the **Open Challenge** of WRO Future Engineers 2025. The robot must autonomously drive three laps while maintaining proper distance and direction using gyroscopic and ultrasonic feedback.

---

## Imports and Sensor Setup

```vbnet
import "Mods\AdvEncoder"
import "Mods\AdvGyro"
import "Mods\ColorRGB"
import "Mods\SteerControl"
import "Mods\AdvUltrasonic"
import "Mods\Tool"
```

These are custom libraries used for handling sensors and control systems:
- **AdvGyro**: For calibrated gyro usage and reset handling
- **SteerControl**: Implements a PID steering controller
- **ColorRGB**: For calibrated color sensing
- **AdvUltrasonic**: Ultrasonic distance sensors (left & right)
- **Tool**: Utilities for math operations and selection logic

---

## Sensor Modes and Gyro Initialization

```vbnet
Sensor.SetMode(1, 0)
Sensor.SetMode(2, 0)
Sensor.SetMode(3, 4)
Sensor.SetMode(4, 0)
```

Sensor port configurations:
- Port 1: Ultrasonic (right)
- Port 2: Gyro sensor
- Port 3: Color sensor in RGB mode
- Port 4: Ultrasonic (left)

```vbnet
AdvGyro.CheckReset(2, result)
While result = 0
  Program.Delay(1000)
  AdvGyro.HardReset(2)
  AdvGyro.CheckReset(2, result)
EndWhile
```

Resets the gyro sensor on port 2. The loop waits until it's confirmed reset.

---

## Color Calibration Loading

```vbnet
col = EV3File.OpenRead("col")
Rmin = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Rmax = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Gmin = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Gmax = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Bmin = EV3File.ConvertToNumber(EV3File.ReadLine(col))
Bmax = EV3File.ConvertToNumber(EV3File.ReadLine(col))
ColorRGB.Config(Rmin, Rmax, Gmin, Gmax, Bmin, Bmax)
```

Loads the previously saved RGB calibration values (from `Calibration.bp`) and configures the color module accordingly.

---

## Subsystems Configuration and Variables

```vbnet
AdvGyro.ResetPort2(0)
AdvEncoder.Config()
SteerControl.Config(1.5, 0.05, 3, 40, 77)
```

Initializes the gyro, encoders, and sets PID parameters for steering control.

```vbnet
MotorC.StartPower(-80)
Program.Delay(2000)
MotorC.ResetCount()
```

Prepares steering motor C: spins it briefly then resets its encoder count.

```vbnet
angleKp = 0.7
angleKd = 1
angleOld = 0
clockWise = 0
turnCounter = 0
turnAngle = 88
UArtReady = 0
SteeringReady = 0
DisplayReady = 0
aimx=30
distance=2000
```

Variables for PID steering, state management, and target angle handling.

---

## Threads: Sensor Input, Steering, and Display

### UArt (sensor update thread)
```vbnet
Sub UArt
  UArtReady = 1
  While 1=1
    AdvGyro.WritePort2(gyroAngle)
    ColorRGB.ReadPort3(r, g, b)
    AdvUltrasonic.ReadPort1(RDistance)
    AdvUltrasonic.ReadPort4(LDistance)
  EndWhile
EndSub
```
Continuously updates gyro angle, RGB values, and distances from both ultrasonic sensors.

---

### Steering thread (PID loop)
```vbnet
Sub Steering
  SteeringReady = 1
  While 1=1
    SteerControl.Core(MotorC.GetTacho(), powerC)
    MotorC.StartPower(powerC)
  EndWhile
EndSub
```
Keeps the steering motor aligned based on the current target angle via PID.

---

### Display thread (debug view)
```vbnet
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
Displays current RGB values and `isWhite` detection on screen for debugging.

---

## Supporting Functions

### Color Classification
```vbnet
Function ColorCheck(out number isWhite, out number isOrange)
  If @b < 50 Then
    isWhite = 0
  Else
    isWhite = 1
  EndIf
  If @r > 85 Then
    isOrange = 1
  Else
    isOrange = 0
  EndIf
EndFunction
```
Checks if surface is white or orange based on calibrated RGB readings.

---

### PID Steering Target Calculation
```vbnet
Function AngleCore(in number angle, out number aim)
  aim = @angleKp * angle + @angleKd * (angle - @angleOld)
  @angleOld = angle
EndFunction
```
Computes next steering target angle based on gyro angle error.

---

### Turn Reset
```vbnet
Function Reset(in number turnAngle)
  If @clockWise = 0 Then
    AdvGyro.ResetPort2(@gyroAngle + turnAngle)
  Else
    AdvGyro.ResetPort2(@gyroAngle - turnAngle)
  EndIf
  AdvGyro.WritePort2(@gyroAngle)
  @turnCounter++
  Time.Reset1()
EndFunction
```
Resets gyro after each turn and counts laps.

---

### Wall-Centering Logic
```vbnet
Function Center()
  Tool.select(@clockwise, @LDistance, @RDistance, Distance)
  If Distance > 100 Then
    Distance = 0
  EndIf
  Distance = Math.Cos(Math.GetRadians(@gyroAngle * 1.3)) * Distance
  Tool.select(@clockwise,Distance-@aimx,@aimx-Distance,Distance) 
  Tool.constrain(Distance,-25,25,U)
  AngleCore((@gyroAngle+U)*1.5,aim)
  SteerControl.SetTarget(aim)
EndFunction
```
Calculates optimal steering based on side wall distances to keep robot centered.

---

## Start Routine

```vbnet
Function Start()
  isWhite = 1
  isOrange = 0
  MotorAB.StartPower(50)
  Time.Reset1()
  While isWhite = 1 Or Time.Get1() < 1000
    AngleCore(@gyroAngle, angle)
    SteerControl.SetTarget(angle)
    ColorCheck(isWhite, isOrange)
  EndWhile 
  @clockwise = isOrange 
  Speaker.Tone(50, 3000, 100)

  Tool.select(@clockwise, @LDistance, @RDistance, Distance)
  If Distance >= 50 Then
    arriv = 200
  Else
    If Distance >= 39 Then
      arriv = 100
    Else
      arriv = 35
    EndIf
  EndIf
  MotorA.ResetCount()
  While MotorA.GetTacho()<arriv
    Center()
  EndWhile

  Reset(@turnAngle)
EndFunction
```

Robot moves forward until see the line or timeout, checks direction (orange line = clockwise), calculates how far to go before first turn, and centers before resetting gyro.

---

## Main Loop: Navigate 3 Laps

```vbnet
Thread.Run = UArt
Thread.Run = Steering
Thread.Run = Display

While UArtReady = 0 Or SteeringReady = 0 Or DisplayReady = 0
EndWhile

Start()
MotorAB.StartPower(100)

While turnCounter<12
  isWhite = 1
  isOrange = 0
  While @clockWise<>isOrange Or isWhite=1 Or Time.Get1() < 2000 
    Center()
    ColorCheck(isWhite, isOrange)
  EndWhile
  Speaker.Tone(50, 3000, 100)
  Reset(turnAngle)
  Time.Reset1()
EndWhile
```

- Threads are started
- Robot drives forward, detects color markers at each turn
- After each turn, gyro is re-zeroed
- 12 turns = 3 full laps

---

## Finish Logic

```vbnet
MotorA.ResetCount()
While MotorA.GetTacho()<1500
  Center()
EndWhile

MotorAB.OffAndBrake()
Speaker.Tone(100, 3000, 300)
Speaker.Wait()
Speaker.Tone(100, 3000, 300)
Speaker.Wait()
Speaker.Tone(100, 3000, 300)
Speaker.Wait()
```

After 3 laps, robot moves into the starting zone and stops, playing a celebratory tone.

---
