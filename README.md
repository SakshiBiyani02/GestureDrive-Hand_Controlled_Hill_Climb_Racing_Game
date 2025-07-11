# GestureDrive
Control your Hill Climb Racing game using simple hand gestures with your webcam! GestureDrive uses MediaPipe and OpenCV to detect hand movements and translates them into keyboard inputs — turning your hand into a racing controller.
## Features
Open Palm 🖐️ → Accelerate (Right Arrow)

Fist ✊ → Brake (Left Arrow)

No Gesture / Other Gestures 🤚 → Neutral (No key press)

Real-time hand tracking with MediaPipe

Seamless gesture-to-keyboard mapping via PyAutoGUI

Live webcam feed with gesture status overlay

## Tech Stack
OpenCV – For webcam access and image processing

MediaPipe – For hand detection and landmark tracking

PyAutoGUI – For simulating keyboard input

## How to Use
Launch the script:
python hill.py
Ensure your webcam is active and your hand is visible on screen.

Use these gestures:

🖐️ Open Palm → Accelerate (Right Arrow)

![Img1](https://github.com/SakshiBiyani02/GestureDrive-Hand_Controlled_Hill_Climb_Racing_Game/blob/main/Screenshot%202025-07-11%20230728.png?raw=true)

✊ Fist → Brake (Left Arrow)

![Img2](https://github.com/SakshiBiyani02/GestureDrive-Hand_Controlled_Hill_Climb_Racing_Game/blob/main/Screenshot%202025-07-11%20230747.png?raw=true)

🤚 Other Gestures / No Hand → Neutral (No key press)

![Img3](https://github.com/SakshiBiyani02/GestureDrive-Hand_Controlled_Hill_Climb_Racing_Game/blob/main/Screenshot%202025-07-11%20230846.png?raw=true)

Open the Hill Climb Racing game window and enjoy gesture-based control!

![game](https://github.com/SakshiBiyani02/GestureDrive-Hand_Controlled_Hill_Climb_Racing_Game/blob/main/Screenshot%202025-07-11%20231236.png?raw=true)

## How It Works
This project uses hand gesture recognition to simulate keyboard inputs for controlling applications (e.g., games). Here's how it works step by step:

🖐️ 1. Hand Landmark Detection (MediaPipe)
- Uses MediaPipe Hands to process the webcam feed in real-time.

- Detects 21 hand landmarks, including fingertips, finger joints, and the wrist.

Provides precise tracking of hand position and finger orientation.

✋ 2. Finger State Detection
A function determines whether each finger (excluding the thumb) is up or down.

For each finger:

- Compares the y-coordinate of the fingertip with its corresponding PIP joint.

- If the fingertip is higher (i.e., lower y-value on screen), the finger is considered up.

3. Gesture-to-Action Mapping
   
The number of raised fingers is used to trigger specific actions:

4 fingers up → Open Palm

🟢 Action: Accelerate (simulate pressing "w")

0 fingers up → Fist

🔴 Action: Brake (simulate pressing "s")

1–3 fingers up → Any other gesture

⚪ Action: Neutral (no input sent)

4. Keyboard Simulation (PyAutoGUI)
- Uses PyAutoGUI to simulate keyboard input based on the recognized gesture.

- Automatically presses or releases keys depending on the current hand pose.

- Enables touchless control for games, robotics, or other interactive applications.

## Conclusion
This project demonstrates a simple yet powerful way to control applications using hand gestures and computer vision. By combining MediaPipe for hand tracking with PyAutoGUI for keyboard automation, it offers an intuitive, touch-free interface that can be extended to games, robotics, and accessibility tools. Customize the gesture mappings and actions to suit your own creative use cases!


