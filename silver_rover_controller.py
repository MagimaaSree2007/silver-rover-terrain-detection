
from controller import Robot
import math

# =====================================================
# 1. ROBOT INITIALIZATION
# =====================================================

robot = Robot()
timestep = int(robot.getBasicTimeStep())

print("====================================", flush=True)
print("     SILVER ROVER STARTED", flush=True)
print("====================================", flush=True)


# =====================================================
# 2. IMU SENSOR INITIALIZATION
# =====================================================

accelerometer = robot.getDevice("accelerometer")
gyro = robot.getDevice("gyro")
imu = robot.getDevice("inertial unit")

# Check whether all IMU sensors are available
if accelerometer is None:
    raise RuntimeError("Accelerometer not found!")

if gyro is None:
    raise RuntimeError("Gyro not found!")

if imu is None:
    raise RuntimeError("InertialUnit not found!")

# Enable sensors
accelerometer.enable(timestep)
gyro.enable(timestep)
imu.enable(timestep)

print("IMU sensors enabled successfully!", flush=True)


# =====================================================
# 3. FOUR MOTOR INITIALIZATION
# =====================================================

motor_names = [
    "front left wheel",
    "front right wheel",
    "back left wheel",
    "back right wheel"
]

motors = []

for name in motor_names:

    motor = robot.getDevice(name)

    if motor is None:
        raise RuntimeError("Motor not found: " + name)

    motor.setPosition(float("inf"))
    motor.setVelocity(0.0)

    motors.append(motor)

print("All four wheel motors initialized!", flush=True)


# =====================================================
# 4. WHEEL SENSOR INITIALIZATION
# =====================================================

sensor_names = [
    "front left wheel sensor",
    "front right wheel sensor",
    "back left wheel sensor",
    "back right wheel sensor"
]

wheel_sensors = []

for name in sensor_names:

    sensor = robot.getDevice(name)

    if sensor is None:
        raise RuntimeError("Wheel sensor not found: " + name)

    sensor.enable(timestep)
    wheel_sensors.append(sensor)

print("All four wheel sensors enabled!", flush=True)


# =====================================================
# 5. TERRAIN DETECTION PARAMETERS
# =====================================================

MAX_SPEED = 3.0

SLOPE_ANGLE = 15.0
DANGEROUS_TILT = 35.0

# Initial impact threshold; tune during testing
IMPACT_THRESHOLD = 18.0

# Speed factors
FLAT_SPEED = 1.0
SLOPE_SPEED = 0.65
ROUGH_SPEED = 0.40
STOP_SPEED = 0.0


# =====================================================
# 6. ADAPTIVE TERRAIN DETECTION
# =====================================================

print("Starting terrain detection...", flush=True)

while robot.step(timestep) != -1:

    # -------------------------------------------------
    # Read IMU measurements
    # -------------------------------------------------

    accel = accelerometer.getValues()
    gyro_values = gyro.getValues()
    rpy = imu.getRollPitchYaw()

    # Convert radians to degrees
    roll = math.degrees(rpy[0])
    pitch = math.degrees(rpy[1])
    yaw = math.degrees(rpy[2])

    # Calculate acceleration magnitude
    accel_mag = math.sqrt(
        accel[0] ** 2 +
        accel[1] ** 2 +
        accel[2] ** 2
    )

    # -------------------------------------------------
    # Terrain classification
    # -------------------------------------------------

    terrain = "FLAT"
    speed_factor = FLAT_SPEED

    # Dangerous tilt: highest priority
    if (
        abs(roll) >= DANGEROUS_TILT or
        abs(pitch) >= DANGEROUS_TILT
    ):

        terrain = "HIGH_TILT"
        speed_factor = STOP_SPEED

    # Rough terrain / possible impact
    elif accel_mag >= IMPACT_THRESHOLD:

        terrain = "ROUGH"
        speed_factor = ROUGH_SPEED

    # Side slope
    elif abs(roll) >= SLOPE_ANGLE:

        terrain = "SIDE_SLOPE"
        speed_factor = SLOPE_SPEED

    # Forward or backward slope
    elif abs(pitch) >= SLOPE_ANGLE:

        terrain = "SLOPE"
        speed_factor = SLOPE_SPEED

    # -------------------------------------------------
    # Adaptive motor speed control
    # -------------------------------------------------

    target_speed = MAX_SPEED * speed_factor

    for motor in motors:
        motor.setVelocity(target_speed)

    # -------------------------------------------------
    # Read wheel encoder positions
    # -------------------------------------------------

    wheel_positions = []

    for sensor in wheel_sensors:
        position = sensor.getValue()
        wheel_positions.append(position)

    # -------------------------------------------------
    # Display results
    # -------------------------------------------------

    print(
        f"Terrain: {terrain} | "
        f"Pitch: {pitch:.2f} deg | "
        f"Roll: {roll:.2f} deg | "
        f"Yaw: {yaw:.2f} deg | "
        f"Acceleration: {accel_mag:.2f} m/s2 | "
        f"Speed: {target_speed:.2f} rad/s"
    , flush=True)

    print(
        "Wheel positions: "
        f"FL={wheel_positions[0]:.2f}, "
        f"FR={wheel_positions[1]:.2f}, "
        f"BL={wheel_positions[2]:.2f}, "
        f"BR={wheel_positions[3]:.2f}",
        flush=True
    )


print("Silver Rover simulation stopped!", flush=True)







