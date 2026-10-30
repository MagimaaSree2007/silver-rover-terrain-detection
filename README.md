# Silver Rover — Terrain Detection & Adaptive Motor Speed Control

## 1. Project Overview

Silver Rover is a robotics simulation project developed using Webots and Python. The project focuses on terrain detection and adaptive motor speed control to help a rover respond to different terrain conditions.

The rover simulation is designed to explore how terrain information can be used to adjust motor speeds and improve movement stability across different surfaces.

## 2. Objectives

- Simulate a rover using the Webots robotics simulator.
- Monitor rover movement using simulated sensor information.
- Detect terrain conditions using threshold-based logic.
- Adjust motor speeds according to detected terrain conditions.
- Explore rover stability and movement across different terrains.
- Provide a foundation for future hardware implementation and testing.

## 3. Technologies Used

- **Webots:** Robotics simulation and environment modeling.
- **Python:** Rover controller programming.
- **Threshold-Based Detection:** Classification of terrain conditions using sensor values.
- **Adaptive Motor Control:** Adjusting motor speed according to detected conditions.

## 4. Project Files

The repository contains the following files:

| File | Description |
|---|---|
| `silver_rover_simulation.wbt` | Webots world file containing the rover simulation environment. |
| `silver_rover_controller.py` | Python controller for rover behavior, terrain detection, and motor control. |
| `.silver_rover_simulation.wbproj` | Webots project configuration file. |
| `.silver_rover_simulation.jpg` | Image associated with the rover simulation. |

## 5. How It Works

The project follows these general steps:

1. **Sensor Monitoring:** The controller obtains available simulated sensor readings.
2. **Terrain Detection:** Sensor values are evaluated using threshold-based logic to identify terrain conditions.
3. **Motor Speed Adjustment:** Motor speeds are adjusted according to the detected condition.
4. **Rover Movement:** The rover responds to the controller's motor commands in the Webots environment.
5. **Simulation Testing:** Rover behavior can be observed under different simulated conditions.

## 6. How to Run the Project

### Prerequisites

- Webots robotics simulator.
- Python environment supported by the installed Webots version.

### Instructions

1. Clone or download this repository.
2. Open Webots.
3. Open the world file `silver_rover_simulation.wbt`.
4. Ensure that the controller is correctly associated with the rover.
5. Click the **Play** button to start the simulation.
6. Observe the rover's movement and controller behavior.

**Note:** If Webots reports missing resources, ensure that any required project dependencies are installed and available.

## 7. Testing and Validation

The project can be tested by observing rover movement and controller responses in the Webots simulation.

Suggested tests include:

- Testing movement on flat terrain.
- Testing movement on inclined terrain.
- Observing sensor readings during movement.
- Checking motor speed changes under different detected conditions.
- Evaluating rover behavior when the sensor readings exceed configured thresholds.

Actual performance should be evaluated using simulation results and recorded observations.

## 8. Current Status

The Webots simulation has been opened and tested successfully.

Further testing can focus on terrain classification accuracy, motor speed adaptation, rover stability, and performance across different simulated surfaces.

## 9. Future Enhancements

- Improve terrain classification using additional sensor data.
- Integrate an IMU for pitch, roll, and acceleration measurements.
- Incorporate wheel encoder feedback where available.
- Implement independent adaptive control for all four motors.
- Test the controller across multiple terrain types.
- Integrate a dashboard for visualizing sensor readings and motor speeds.
- Transfer the control system to physical rover hardware when available.

## 10. Conclusion

Silver Rover provides a simulation-based foundation for exploring terrain detection and adaptive motor speed control in robotics. Using Webots and Python, the project can be extended to evaluate rover behavior, improve control strategies, and prepare for future real-world implementation.

---

**Project Name:** Silver Rover — Terrain Detection & Adaptive Motor Speed Control  
**Simulation Platform:** Webots  
**Programming Language:** Python
