# `Calibration.bp` program explanation

This document explains our `Calibration.bp` program. It calibrates the color sensor by rotating and capturing min/max RGB values on the ground, saving them for use in later programs like `Open2.bp` and `Obstacle2.bp`.

---

## Purpose

- Normalize lighting and surface colors.
- Save calibrated min/max RGB values into a file called `col`.

---

## Code Breakdown

### Sensor Mode and Initial Motor Spin

```vbnet
Sensor.SetMode(3, 4)
MotorC.StartPower(50)
Program.Delay(2000)
```

- Sets **Port 3** (color sensor) to RGB mode.
- Starts **Motor C** (likely turning sensor or camera platform).
- Waits 2 seconds for stabilization.

---

### Backward Drive and Movement Start

```vbnet
Motor.Move("C", -50, 54, "True")
MotorAB.StartPower(50)
```

- Motor C moves backward for 54 degrees.
- Both A and B motors begin driving forward to traverse the surface.

---

### Initialization of Min/Max RGB Variables

```vbnet
LCD.Clear()
Rmin = 500
Gmin = 500
Bmin = 500
Rmax = -500
Gmax = -500
Bmax = -500
```

Initial extreme values set to detect true minimum and maximum values seen during scan.

---

### File Creation and Sensor Variables

```vbnet
col = EV3File.OpenWrite("col")
r = 0
g = 0
b = 0
```

Opens file `col` for writing and initializes local RGB reading variables.

---

### Main Calibration Loop

```vbnet
While MotorA.GetTacho() < 400
  Sensor3.Raw3(r, g, b)
  Rmin = Math.Min(Rmin, r)
  Rmax = Math.Max(Rmax, r)
  Gmin = Math.Min(Gmin, g)
  Gmax = Math.Max(Gmax, g)
  Bmin = Math.Min(Bmin, b)
  Bmax = Math.Max(Bmax, b)
EndWhile
```

- While motor A travels forward (encoder < 400), continuously read RGB values.
- Keep track of lowest and highest values for each channel.

---

### Save Values to File

```vbnet
EV3File.WriteLine(col, Rmin)
EV3File.WriteLine(col, Rmax)
EV3File.WriteLine(col, Bmin)
EV3File.WriteLine(col, Bmax)
EV3File.WriteLine(col, Gmin)
EV3File.WriteLine(col, Gmax)
```

Writes all min/max RGB values to the file. **Important note**: the order here is R, B, G instead of R, G, B. This should be kept consistent when reading.

---

## 📁 Output

The file `col` will contain:
1. Minimum Red
2. Maximum Red
3. Minimum Blue
4. Maximum Blue
5. Minimum Green
6. Maximum Green

These are later used in:
- `ColorRGB.Config()` for normalizing sensor input
- Consistent color detection across lighting conditions

---

## ✅ Summary

This calibration routine is essential for robust RGB-based color classification. It helps in reliably distinguishing between white lines, black roads, and colored markers.

