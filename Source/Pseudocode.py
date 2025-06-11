START PROGRAM

Initialize sensors:
  - Set Pixy2 (I2C), Ultrasonic, Gyro, Color Sensor modes
  - Load RGB calibration values from file
  - Configure PID for steering

Start Threads:
  - Sensor Thread: constantly updates gyro angle, ultrasonic distance, RGB color
  - Pixy2 Thread: tracks largest object, gets x/y and signature
  - Steering Thread: PID adjusts steering motor based on target angle

Wait until all threads are ready

FUNCTION Start():
  Start moving forward
  While surface is white:
    - Use Autopilot mode 1 (just gyro-based correction)
    - Check for orange turn marker
  Determine turn direction (clockwise if orange detected)
  Play tone and reset gyro heading for first turn

MAIN LOOP (repeat 12 turns):
  While orange turn marker not detected OR wrong direction:
    - Use Autopilot mode 0 (obstacle avoidance active)
    - Check if orange is detected and direction matches
  When turn point is valid:
    - Play tone and reset gyro heading

FUNCTION Autopilot(variant):
  IF no object detected by Pixy2 OR ultrasonic distance out of range:
    - IF variant = 0: use wall-centering logic (Center())
    - ELSE: just use gyro-based correction
  ELSE:
    - Run DetourObstacle()

FUNCTION DetourObstacle():
  - IF signature = 2 (e.g., green block):
      use mirrored parabola to calculate desired X
  - ELSE (e.g., red block):
      use standard parabola for trajectory
  - Set target steering angle to follow curve (difference between desired X and Pixy2 X)

FUNCTION Center():
  - Maintain 44 cm distance to wall using gyro and ultrasonic
  - Adjust steering angle with PID based on difference

After 12 turns:
  Drive forward until encoder reaches finish
  Brake motors and play 3 final tones

END PROGRAM
