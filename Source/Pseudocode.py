INITIALIZE sensors (gyro, color, ultrasonic, pixycam)
RESET gyro until stable
LOAD color calibration from file
CONFIGURE steering PID and encoder
CALIBRATE steering motor

SET constants (Kp, Kd, turnAngle, etc.)
START threads:
  - UART: read gyro, color, distance
  - I2C: read Pixy object data
  - Steering: maintain PID steering
  - Display: show distance on LCD

WAIT until all threads ready
EXECUTE GetOutOfParking()

FUNCTION Start():
  drive forward until orange marker detected
  set turn direction (clockwise / counterclockwise)
  play tone
  call Reset(turnAngle)

MAIN LOOP (12 turns total):
  while not at next orange marker:
    if no obstacle or far distance → Center()
    else → DetourObstacle()
  play tone
  call Reset(turnAngle)

FUNCTION Center():
  compute distance correction using gyro + ultrasonic
  adjust steering to stay centered

FUNCTION DetourObstacle():
  use Pixy camera to detect obstacle position
  compute steering correction around obstacle

FUNCTION Reset(turnAngle):
  reset gyro reference based on turn direction
  increment turn counter
  reset timer

AFTER 12 turns:
  drive straight to finish zone
  make final rotations (90°, 180°, etc.)
  stop motors and play 3 finish tones
