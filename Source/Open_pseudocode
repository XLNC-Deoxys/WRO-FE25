INITIALIZE sensors (gyro, color, two ultrasonic)
RESET gyro until stable
LOAD color calibration from file
CONFIGURE steering PID and encoder
CALIBRATE steering motor position

SET constants (Kp, Kd, turnAngle, etc.)
START threads:
  - UART: read gyro, color, left/right distance
  - Steering: run PID steering loop
  - Display: show color data on LCD

WAIT until all threads ready

FUNCTION Start():
  drive forward while surface is white
  detect orange marker → set turn direction (clockwise / counterclockwise)
  estimate distance to wall (based on ultrasonic)
  drive forward predetermined distance (depends on wall range)
  call Reset(turnAngle)

MAIN LOOP (12 turns total):
  while not at next orange marker:
    keep Center() to stay between left/right walls
    update colors
  drive small distance forward
  play tone
  call Reset(turnAngle)
  reset timer

FUNCTION Center():
  measure both ultrasonic distances (left and right)
  compute offset from center
  correct steering using gyro + PD controller

FUNCTION Reset(turnAngle):
  reset gyro reference based on turn direction
  increment turn counter

AFTER 12 turns:
  drive straight toward finish line while centering
  stop and brake motors
  play 3 finish tones
