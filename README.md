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

✊ Fist → Brake (Left Arrow)

🤚 Other Gestures / No Hand → Neutral (No key press)

Open the Hill Climb Racing game window and enjoy gesture-based control!

## How It Works
The webcam feed is processed with MediaPipe to detect 21 hand landmarks.

A function checks if fingers (excluding thumb) are up by comparing the y-coordinates of fingertip and PIP joints.
Depending on the number of raised fingers:
4 fingers up = Open Palm → Accelerate
0 fingers up = Fist → Brake
Any other count = Neutral
Keyboard inputs are simulated using PyAutoGUI.

