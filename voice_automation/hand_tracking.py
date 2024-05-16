import cv2
import mediapipe as mp
import voice_automation

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def trigger_voice_assistant():
    voice_automation.respond("How can I assist you?")

def is_hey_ayana_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # Debugging information
    print(f"Thumb Tip: {thumb_tip.y}, Index Finger Tip: {index_finger_tip.y}, Wrist: {wrist.y}")

    # Condition for "Hey Ayana" gesture
    if (thumb_tip.y < wrist.y and
        index_finger_tip.y < wrist.y and
        middle_finger_tip.y > wrist.y and
        ring_finger_tip.y > wrist.y and
        pinky_tip.y > wrist.y):
        print("Hey Ayana gesture detected!")
        return True
    return False

def detect_gesture(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks and connections on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_hey_ayana_gesture(hand_landmarks):
                return True
    return False

def process_gesture():
    cap = cv2.VideoCapture(0)
    gesture_detected = False
    stable_count = 0
    stable_threshold = 5  # Number of frames the gesture needs to be consistently detected

    try:
        while cap.isOpened() and not gesture_detected:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            if detect_gesture(frame):
                stable_count += 1
                if stable_count >= stable_threshold:
                    trigger_voice_assistant()
                    gesture_detected = True
            else:
                stable_count = 0  # Reset if the gesture is not consistently detected

            cv2.imshow('Hand Tracking', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    process_gesture()
