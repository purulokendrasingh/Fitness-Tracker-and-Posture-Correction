import numpy as np
import pandas as pd
import mediapipe as mp
import cv2

mediapipe_pose = mp.solutions.pose

# Calculates the angle at p2 by p1 and p3 joints
def calculate_joint_angle(p1, p2, p3):
    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)

    angle_in_radians = np.arctan2(p3[1] - p2[1], p3[0] - p2[0]) - np.arctan2(p1[1] - p2[1], p1[0] - p2[0])
    angle_in_degrees = np.abs(angle_in_radians * 180.0 / np.pi)

    if angle_in_degrees > 180.0:
        angle_in_degrees = 360 - angle_in_degrees

    return angle_in_degrees


# Detect body part joint given the landmark and joint name
def detect_joint(lm, joint_name):
    return [
        lm[mediapipe_pose.PoseLandmark[joint_name].value].x,
        lm[mediapipe_pose.PoseLandmark[joint_name].value].y,
        lm[mediapipe_pose.PoseLandmark[joint_name].value].visibility
    ]


# Detect body parts on the basis of landmark
def detect_joints(lm):
    body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

    for i, lk in enumerate(mediapipe_pose.PoseLandmark):
        lk = str(lk).split(".")[1]
        cord = detect_joint(lm, lk)
        body_parts.loc[i] = lk, cord[0], cord[1]

    return body_parts


# Utility function for displaying the attributes on screen
def display_table(exercise, frame , counter, status, displayPos):
    cv2.putText(frame, "Activity : " + exercise.replace("-", " "),
                (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2,
                cv2.LINE_AA)
    cv2.putText(frame, "Counter : " + str(counter), (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Status : " + str(status), (10, 135),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Posture : " + str(displayPos), (10, 170),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    return frame
    
