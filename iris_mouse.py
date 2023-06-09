
import cv2
import mediapipe as mp
import pyautogui

for i in range(1):
    pyautogui.alert("Make sure you are in good lighting and using a high-res camera.\n"
                    "Enjoy, Pranav Asrani\n"
                    "P.S: Press q to exit")
try:
    # noinspection PyUnresolvedReferences
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    # amplification_factor = 2
    x_offset = screen_w
    y_offset = screen_h
    while True:
        _, frame = cam.read()
        # noinspection PyUnresolvedReferences
        frame = cv2.flip(frame, 1)
        # noinspection PyUnresolvedReferences
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark

            for id, landmark in enumerate(landmarks[474:478]):

                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                # noinspection PyUnresolvedReferences
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:

                    screen_x = screen_w * landmark.x + x_offset
                    screen_y = screen_h * landmark.y + y_offset
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            """
            print("frame_w: {} ".format(frame_w))
            print("frame_h: {} ".format(frame_h))
            """
            if cv2.waitKey(1) == ord('q'):
                break
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                # noinspection PyUnresolvedReferences
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.009:
                pyautogui.click()
                print("click")
                pyautogui.sleep(0.1)
        # noinspection PyUnresolvedReferences
        cv2.imshow('Iris Mouse', frame)


        # noinspection PyUnresolvedReferences
        cv2.waitKey(1)

except pyautogui.FailSafeException as e:
    pyautogui.alert("do not move iris/mouse to edge of screen. may result in infinite loop. instead tilt head so that "
                    "both "
                    "irises stay within the frame")