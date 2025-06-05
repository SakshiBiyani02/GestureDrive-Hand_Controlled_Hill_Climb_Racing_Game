import cv2
import mediapipe as mp
import pyautogui

# Setup MediaPipe and webcam
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Detect if fingers are up (excluding thumb)
def fingers_up(hand_landmarks):
    tips = [8, 12, 16, 20]  # Index to pinky
    fingers = []
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

# Check if hand is a fist (all fingers down)
def is_fist(fingers):
    return sum(fingers) == 0

# Check if hand is open palm (all fingers up)
def is_open_palm(fingers):
    return sum(fingers) == 4

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingers = fingers_up(hand_landmarks)

            if is_open_palm(fingers):
                # Accelerate
                pyautogui.keyDown('right')
                pyautogui.keyUp('left')
                cv2.putText(img, "ACCELERATE (Open Palm)", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            elif is_fist(fingers):
                # Brake
                pyautogui.keyDown('left')
                pyautogui.keyUp('right')
                cv2.putText(img, "BRAKE (Fist)", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            else:
                # Neutral
                pyautogui.keyUp('left')
                pyautogui.keyUp('right')
                cv2.putText(img, "NEUTRAL", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
    else:
        # No hand detected — stop all keys
        pyautogui.keyUp('left')
        pyautogui.keyUp('right')

    # Show camera feed
    cv2.imshow("Sakshi's Project of Hand gesture control ", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
