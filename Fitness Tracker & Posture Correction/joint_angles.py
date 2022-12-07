import numpy as np
import pandas as pd
import cv2
import mediapipe as mp
from utilities import *

class JointAngle:

    def __init__(self, lm):
        self.lm = lm
        
        
    def left_leg_angle(self):
        left_knee = detect_joint(self.lm, "LEFT_KNEE")
        left_hip = detect_joint(self.lm, "LEFT_HIP")
        left_ankle = detect_joint(self.lm, "LEFT_ANKLE")
        return calculate_joint_angle(left_hip, left_knee, left_ankle)
        

    def right_leg_angle(self):
        right_hip = detect_joint(self.lm, "RIGHT_HIP")
        right_ankle = detect_joint(self.lm, "RIGHT_ANKLE")
        right_knee = detect_joint(self.lm, "RIGHT_KNEE")
        
        return calculate_joint_angle(right_hip, right_knee, right_ankle)
        

    def neck_angle(self):
        right_shoulder = detect_joint(self.lm, "RIGHT_SHOULDER")
        left_shoulder = detect_joint(self.lm, "LEFT_SHOULDER")
        right_hip = detect_joint(self.lm, "RIGHT_HIP")
        left_hip = detect_joint(self.lm, "LEFT_HIP")
        right_mouth = detect_joint(self.lm, "MOUTH_RIGHT")
        left_mouth = detect_joint(self.lm, "MOUTH_LEFT")

        shoulder_angle = [(right_shoulder[0] + left_shoulder[0]) / 2,
                        (right_shoulder[1] + left_shoulder[1]) / 2]
        mouth_angle = [(right_mouth[0] + left_mouth[0]) / 2,
                     (right_mouth[1] + left_mouth[1]) / 2]
        hip_angle = [(right_hip[0] + left_hip[0]) / 2, (right_hip[1] + left_hip[1]) / 2]

        return abs(180 - calculate_joint_angle(mouth_angle, shoulder_angle, hip_angle))
        

    def left_arm_angle(self):
        left_shoulder = detect_joint(self.lm, "LEFT_SHOULDER")
        left_elbow = detect_joint(self.lm, "LEFT_ELBOW")
        left_wrist = detect_joint(self.lm, "LEFT_WRIST")
        return calculate_joint_angle(left_shoulder, left_elbow, left_wrist)
        
    
    def right_arm_angle(self):
        right_shoulder = detect_joint(self.lm, "RIGHT_SHOULDER")
        right_elbow = detect_joint(self.lm, "RIGHT_ELBOW")
        right_wrist = detect_joint(self.lm, "RIGHT_WRIST")
        return calculate_joint_angle(right_shoulder, right_elbow, right_wrist)
        

    def abdomen_angle(self):
        right_shoulder = detect_joint(self.lm, "RIGHT_SHOULDER")
        left_shoulder = detect_joint(self.lm, "LEFT_SHOULDER")
        shoulder_anglr = [(right_shoulder[0] + left_shoulder[0]) / 2,
                        (right_shoulder[1] + left_shoulder[1]) / 2]

        right_hip = detect_joint(self.lm, "RIGHT_HIP")
        left_hip = detect_joint(self.lm, "LEFT_HIP")
        hip_angle = [(right_hip[0] + left_hip[0]) / 2, (right_hip[1] + left_hip[1]) / 2]

        right_knee = detect_joint(self.lm, "RIGHT_KNEE")
        left_knee = detect_joint(self.lm, "LEFT_KNEE")
        knee_angle = [(r_knee[0] + l_knee[0]) / 2, (r_knee[1] + l_knee[1]) / 2]

        return calculate_joint_angle(shoulder_angle, hip_angle, knee_angle)
        
        
    def back_angle(self):
        right_shoulder = detect_joint(self.lm, "RIGHT_SHOULDER")
        left_shoulder = detect_joint(self.lm, "LEFT_SHOULDER")
        shoulder_angle = [(right_shoulder[0] + left_shoulder[0]) / 2,
                        (right_shoulder[1] + left_shoulder[1]) / 2]

        right_hip = detect_joint(self.lm, "RIGHT_HIP")
        left_hip = detect_joint(self.lm, "LEFT_HIP")
        hip_angle = [(right_hip[0] + left_hip[0]) / 2, (right_hip[1] + left_hip[1]) / 2]

        ref_angle = [hip_angle[0], shoulder_angle[1]]

        return calculate_joint_angle(shoulder_angle, hip_angle, ref_angle)
