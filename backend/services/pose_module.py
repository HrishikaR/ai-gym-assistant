import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


# 🔹 Angle calculation
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
              np.arctan2(a[1]-b[1], a[0]-b[0])

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle

    return angle


# 🔥 Personalized workout plan
def get_workout_plan(score):
    if score < 50:
        return "Beginner", [
            "Squats – 3x10",
            "Wall Push-ups – 3x8",
            "Plank – 20 sec"
        ]
    elif score < 80:
        return "Intermediate", [
            "Squats – 4x12",
            "Push-ups – 4x10",
            "Lunges – 3x12",
            "Plank – 40 sec"
        ]
    else:
        return "Advanced", [
            "Jump Squats – 4x15",
            "Push-ups – 4x15",
            "Burpees – 3x10",
            "Plank – 60 sec"
        ]


# 🔥 MAIN STREAM FUNCTION
def generate_frames():
    cap = cv2.VideoCapture(0)

    counter = 0
    stage = None
    good_reps = 0
    bad_reps = 0
    min_angle = 180

    with mp_pose.Pose(min_detection_confidence=0.5,
                      min_tracking_confidence=0.5) as pose:

        while True:
            success, frame = cap.read()
            if not success:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark

                # 🔹 Key points
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                # 🔹 Angles
                angle = calculate_angle(hip, knee, ankle)
                back_angle = calculate_angle(shoulder, hip, knee)

                if angle < min_angle:
                    min_angle = angle

                # 🔥 REP COUNT
                if angle < 90:
                    stage = "down"

                if angle > 160 and stage == "down":
                    stage = "up"
                    counter += 1

                    if min_angle < 90 and back_angle > 150:
                        good_reps += 1
                    else:
                        bad_reps += 1

                    min_angle = 180

                # 🔥 FEEDBACK
                feedback = "Keep Going"

                if back_angle < 150:
                    feedback = "Back Bent ❌"
                elif min_angle > 100 and stage == "down":
                    feedback = "Go Lower ⬇️"
                elif min_angle < 90:
                    feedback = "Good Depth ✅"

                # 🔹 SCORE
                score = (good_reps / (counter + 1e-5)) * 100

                # 🔥 WORKOUT PLAN
                level, workout_plan = get_workout_plan(score)

                # 🔥 UI PANEL
                cv2.rectangle(image, (0, 0), (250,140), (0, 0, 0), -1)

                cv2.putText(image, f'Reps: {counter}', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                cv2.putText(image, f'Stage: {stage}', (10, 55),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                cv2.putText(image, f'Feedback: {feedback}', (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

                cv2.putText(image, f'Score: {int(score)}', (10, 110),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

                cv2.putText(image, f'Level: {level}', (10, 140),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                # 🔥 WORKOUT PLAN DISPLAY
                y_offset = 230
                for i, exercise in enumerate(workout_plan):
                    cv2.putText(image, exercise, (10, y_offset + i * 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                # 🔹 Angle display
                cv2.putText(image, str(int(angle)),
                            tuple(np.multiply(knee, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                # 🔹 Draw skeleton
                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS
                )

            # 🔥 STREAM FRAME
            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()