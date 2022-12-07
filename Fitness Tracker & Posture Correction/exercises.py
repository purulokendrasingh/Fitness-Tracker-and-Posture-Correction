import numpy as np
from utilities import *
from joint_angles import JointAngle


class Exercise(JointAngle):

    # Global displayPos param for displaying the posture message
    displayPos = ''
    
    def __init__(self, lm):
        super().__init__(lm)
        
        
    def squat(self, counter, status, displayPos):
        hip_angle = self.abdomen_angle()
        left_leg_angle = self.left_leg_angle()
        right_leg_angle = self.right_leg_angle()
        
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2
        
        if hip_angle < 72:
            displayPos='Increase Hip Angle'

        if status:
            if left_leg_angle < 95 or right_leg_angle < 95:
                displayPos='Go Up'
                if hip_angle<72:
                    displayPos='Up:Increase Hip Angle'
                counter += 1
                status = False
        else:
            if left_leg_angle >169 or right_leg_angle > 169:
                displayPos='Go Down'
                if hip_angle<72:
                    displayPos='Down:Increase Hip Angle'
                status = True
                

        return [counter, status, displayPos]
    

    def push_up(self, counter, status, displayPos):
        left_arm_angle = self.left_arm_angle()
        right_arm_angle = self.right_arm_angle()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 70:
                counter += 1
                status = False
                displayPos='Go Up'
        else:
            if avg_arm_angle > 160:
                status = True
                displayPos='Go Down'

        return [counter, status, displayPos]


    def pull_up(self, counter, status, displayPos):
        nose = detect_joint(self.lm, "NOSE")
        left_wrist = detect_joint(self.lm, "LEFT_WRIST")
        right_wrist = detect_joint(self.lm, "RIGHT_WRIST")
        
        avg_height = (left_wrist[1] + right_wrist[1]) / 2
        
        right_leg = self.right_leg_angle()
        left_leg = self.left_leg_angle()

        if(right_leg < 160 or left_leg < 160):
            displayPos = "Keep Your Legs Straight"
        else:
            displayPos = "Posture is good"

        if status:
            if nose[1] > avg_height:
                counter += 1
                status = False

        else:
            if nose[1] < avg_height:
                status = True

        return [counter, status, displayPos]


    def sit_up(self, counter, status, displayPos):
        angle = self.abdomen_angle()  
            
        if status:
            if angle < 55:
                counter += 1
                displayPos = "Go Down"
                status = False
        else:
            if angle > 105:
                displayPos = "Go Up"
                status = True

        return [counter, status, displayPos]
        
        
    def walk(self, counter, status, displayPos):
        right_knee = detect_joint(self.lm, "RIGHT_KNEE")
        left_knee = detect_joint(self.lm, "LEFT_KNEE")
        right_hip = detect_joint(self.lm, "RIGHT_HIP")
        left_hip = detect_joint(self.lm, "LEFT_HIP")
        right_elbow = detect_joint(self.lm, "RIGHT_ELBOW")
        left_elbow = detect_joint(self.lm, "LEFT_ELBOW")
        right_wrist = detect_joint(self.lm, "RIGHT_WRIST")
        left_wrist = detect_joint(self.lm, "LEFT_WRIST")
        right_shoulder = detect_joint(self.lm, "RIGHT_SHOULDER")
        left_shoulder = detect_joint(self.lm, "LEFT_SHOULDER")
        back_angle = self.back_angle()
        
        shouldProceed = True

        if back_angle < 2:
            displayPos = 'Posture is good'
        else:
            displayPos = 'Correct your posture'
            shouldProceed = False
        
        if shouldProceed:
            if status:
                if left_knee[0] > left_hip[0] and right_knee[0] < left_hip[0]:    
                    counter += 1
                    status = False

            else:
                if left_knee[0] < left_hip[0] and right_knee[0] > left_hip[0]:
                    counter += 1
                    status = True

        return [counter, status, displayPos]
        

    def process_exercise(self, exercise_type, counter, status, displayPos):
        if exercise_type == "push-up":
            counter, status, displayPos = Exercise(self.lm).push_up(
                counter, status, displayPos)
        elif exercise_type == "pull-up":
            counter, status, displayPos = Exercise(self.lm).pull_up(
                counter, status, displayPos)
        elif exercise_type == "sit-up":
            counter, status, displayPos = Exercise(self.lm).sit_up(
                counter, status, displayPos)
        elif exercise_type == "squat":
            counter, status, displayPos = Exercise(self.lm).squat(
                counter, status, displayPos)
        elif exercise_type == "walk":
            counter, status, displayPos = Exercise(self.lm).walk(
                counter, status, displayPos)

        return [counter, status, displayPos]
