# WRO 2025 - `Obstacle2.bp` Program Explanation

This document explains the full logic and structure of the `Obstacle2.bp` program used in the **Obstacle Challenge** of WRO Future Engineers 2025. The robot must autonomously avoid obstacles while following the track and identifying colored turning points. It uses sensors (gyro, color, ultrasonic, and PixyCam) with advanced PID steering.

---

## 📦 Imports and Sensor Setup

```vbnet
import "Mods\AdvEncoder"
import "Mods\AdvGyro"
import "Mods\ColorRGB"
import "Mods\SteerControl"
import "Mods\AdvUltrasonic"
import "Mods\Tool"
import "Mods\AdvPixy"
```

These custom modules handle:
- Encoders, gyroscope and resets
- Steering PID control
- RGB color normalization
- Ultrasonic distance sensing
- PixyCam (for detecting obstacles)

---

```vbnet
Sensor.SetMode(1, 0)
Sensor.SetMode(2, 4)
Sensor.SetMode(3, 0)
```

Sensor setup:
- Port 1: Ultrasonic
- Port 2: Color sensor (raw RGB mode)
- Port 3: Gyroscope

---

## 🔄 Gyroscope Reset Loop

```vbnet
AdvGyro.CheckReset(3, result)
While result = 0
  Program.Delay(1000)
  AdvGyro.HardReset(3)
  AdvGyro.CheckReset(3, result)
EndWhile
```

Ensures gyro on port 3 is properly reset before continuing.

---

## 🎨 Load Color Calibration

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

Loads RGB bounds from calibration file for consistent color detection across environments.

---

## ⚙️ Subsystem Setup

```vbnet
AdvGyro.ResetPort3(0)
AdvEncoder.Config()
SteerControl.Config(1.5, 0.05, 3, 40, 77)
```

Sets up the PID control logic and resets gyro orientation on port 3.

```vbnet
MotorC.StartPower(-80)
Program.Delay(2000)
MotorC.ResetCount()
```

Turns steering motor briefly and resets encoder value.

```vbnet
angleKp = 0.7
angleKd = 1
angleOld = 0
clockWise = 0
turnCounter = 0
turnAngle = 88
UArtReady = 0
I2CReady = 0
SteeringReady = 0
aimx=30
distance=2000
yCameraRange=20
```

Declares variables for PID, control flags, turn angle, and vision targeting.

---

## 🧵 Threads

### UArt Thread (Sensor Updates)

```vbnet
Sub UArt
  UArtReady = 1
  While 1=1
    AdvGyro.WritePort3(gyroAngle)
    ColorRGB.ReadPort2(r, g, b)
    AdvUltrasonic.ReadPort1(Distance)
  EndWhile
EndSub
```

Updates key sensor values continuously: gyro, color, and ultrasonic.

---

### I2C Thread (PixyCam Updates)

```vbnet
Sub I2C
  I2CReady = 1
  While 1=1
    AdvPixy.getLargest(4, pixyX, pixyY, signature)
  EndWhile
EndSub
```

Reads the largest object detected by PixyCam (usually the obstacle block), including its coordinates and signature ID.

---

### Steering PID Thread

```vbnet
Sub Steering
  SteeringReady = 1
  While 1=1
    SteerControl.Core(MotorC.GetTacho(), powerC)
    MotorC.StartPower(powerC)
  EndWhile
EndSub
```

Applies steering power using PID correction.

---

## 🔍 Support Functions

### Color Recognition

```vbnet
Function ColorCheck(out number isWhite, out number isOrange)
  If @b < 55 Then
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

Identifies white background and orange turn points using RGB values.

---

### PID Target Angle Calculation

```vbnet
Function AngleCore(in number angle, out number aim)
  aim = @angleKp * angle + @angleKd * (angle - @angleOld)
  @angleOld = angle
EndFunction
```

Sets the new target angle for steering control based on gyro angle.

---

### Gyro Recalibration

```vbnet
Function Reset(in number turnAngle)
  If @clockWise = 0 Then
    AdvGyro.ResetPort3(@gyroAngle + turnAngle)
  Else
    AdvGyro.ResetPort3(@gyroAngle - turnAngle)
  EndIf
  AdvGyro.WritePort3(@gyroAngle)
  @turnCounter++
  Speaker.Tone(100,300,50)
  Time.Reset1()
EndFunction
```

Resets gyro after each turn and logs a beep. Counts laps.

---

### Obstacle Avoidance Steering

```vbnet
Function DetourObstacle()
  If @signature = 2 Then
    desiredX = -0.0025 * @pixyY * @pixyY + 0.8 * @pixyY + 35
    Speaker.Tone(50, 5000, 20)
  Else
    desiredX = 0.0025 * @pixyY * @pixyY - 0.8 * @pixyY - 35
    Speaker.Tone(50, 500, 20)
  EndIf
  SteerControl.SetTarget((desiredX - @pixyX) * 0.5)
EndFunction
```

Calculates a bypass path around the object using PixyCam data and sets the steering target.

---

### Main Navigation Logic

```vbnet
Function Autopilot(in number variant)
  If @signature = 0 Or @Distance>75 Or @Distance<15 Then
    If variant = 0 Then
      MotorAB.SetPower(40)
      Center()
    Else
      MotorAB.SetPower(40)
      AngleCore(@gyroAngle, angle)
      SteerControl.SetTarget(angle)
    EndIf
  Else
    MotorAB.SetPower(40)
    DetourObstacle()
  EndIf
EndFunction
```

Controls robot behavior:
- Variant 1: use angle only (used at start)
- Variant 0: combine wall-centering with obstacle avoidance

---

### Wall-Centering

```vbnet
Function Center()
  If @Distance >= 100 Then
    temp=1
  Else
    temp=0
  EndIf
  Tool.select(temp, 44, @Distance, dist)
  dist = Math.Cos(Math.GetRadians(@gyroAngle * 1.3)) * dist - 44
  Tool.constrain(dist,-25,25,U)
  AngleCore(@gyroAngle+U,aim)
  SteerControl.SetTarget(aim)
EndFunction
```

Keeps robot aligned with walls using gyro and distance feedback.

---

## 🚦 Start and Main Loop

```vbnet
Function Start()
  isWhite = 1
  isOrange = 0
  MotorAB.StartPower(60)
  While isWhite = 1
    Autopilot(1)
    ColorCheck(isWhite, isOrange)
  EndWhile
  @clockwise = isOrange
  Speaker.Tone(50, 3000, 100)
  arriv=200
  MotorA.ResetCount()
  Reset(@turnAngle)
EndFunction
```

Starts robot and drives until orange is detected. Initializes lap count and turn direction.

---

```vbnet
Thread.Run = UArt
Thread.Run = I2C
Thread.Run = Steering

While UArtReady = 0 Or SteeringReady = 0 Or I2CReady = 0
EndWhile

Start()
```

Starts sensor, PixyCam, and steering threads. Waits for readiness.

---

## 🔁 Main Turn Logic

```vbnet
While turnCounter<12
  isWhite = 1
  isOrange = 0
  While @clockWise<>isOrange Or isWhite=1 Or Time.Get1() < 1500
    Autopilot(0)
    ColorCheck(isWhite, isOrange)
  EndWhile
  Speaker.Tone(50, 3000, 100)
  Reset(turnAngle)
EndWhile
```

Robot turns 12 times (3 laps), detecting turns using color and navigating with obstacle avoidance.

---

## 🏁 Finish

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

After finishing, it drives back into the start zone, stops motors, and plays finish tones.

---
