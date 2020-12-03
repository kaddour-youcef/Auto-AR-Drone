# Auto-AR-Drone
This project is about giving a Parrot AR drone 2.0 the ability to land automatically on a moving platform, using visual tracking and IMU sensors

------------------------------------------------------------------
1 - What should we use? 
- Parrot AR Drone 2.0
- Raspberry Pi 3b+
- Raspberry Pi camera module 
- Mobile platforme Turtel-bot 2.0

2- what are the goals?
- Use the visual data from the camera on the drone to detect and estimate the pose of the moving platform
- Use the IMU data to estimate the pose of the drone 
- apply a kalman filter on boath of the estimations
- Calculate the errors on all the axes 
- use the errors with a PID controller to generate a real time trajectory 
- give the right commands to move the drone 
- Detect the landing
