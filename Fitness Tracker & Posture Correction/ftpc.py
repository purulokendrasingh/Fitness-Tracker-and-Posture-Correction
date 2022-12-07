import argparse
import numpy as np
import pandas as pd
import mediapipe as mp
import cv2
from utilities import *
from joint_angles import JointAngle
from exercises import Exercise

arguement_parser = argparse.ArgumentParser()

arguement_parser.add_argument("-t", "--exercise_type", type=str, help='Type of exercise', required=True)
arguement_parser.add_argument("-vs", "--video_source", type=str, help='Video Source', required=False)
args = vars(arguement_parser.parse_args())
                
args = vars(arguement_parser.parse_args())

mediapipe_pose = mp.solutions.pose
mediapipe_drawing = mp.solutions.drawing_utils

saveVideo = args["video_source"] is not None

if args["video_source"] is not None:
    capture = cv2.VideoCapture("Exercise_Videos/" + args["video_source"])
else:
    capture = cv2.VideoCapture(0)

capture.set(3, 800)
capture.set(4, 480)

with mediapipe_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:

    counter = 0
    status = True
    displayPos = ''
    
    if saveVideo:
        a, ff = capture.read()
        print(ff.shape)
        out = cv2.VideoWriter('Output-Videos/'+args["video_source"][:-4]+'-output.avi', cv2.VideoWriter_fourcc(*'FMP4'), 20.0, (ff.shape[1],ff.shape[0]))
        
    while capture.isOpened():
        ret, frame = capture.read()

        frame = cv2.resize(frame, (frame.shape[1],frame.shape[0]), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False
        results = pose.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (340, 50)
        color = (255,0, 0)
        thickness = 5
        fontScale = 1.5
        
        try:
            lm = results.pose_landmarks.landmark
            counter, status, displayPos = Exercise(lm).process_exercise(
                args["exercise_type"], counter, status, displayPos)
            
        except:
            pass
            
        cv2.rectangle(frame, (10,10), (400,180), (0,0,0), -1)
        cv2.putText(frame, "Exercise : " + args["exercise_type"], 
                    (20,50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        cv2.putText(frame, "Repetition : " + str(counter), 
                    (20,90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        cv2.putText(frame,displayPos, 
                    (20,130), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
        mediapipe_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mediapipe_pose.POSE_CONNECTIONS,
            mediapipe_drawing.DrawingSpec(color=(255, 255, 255),
                                   thickness=2,
                                   circle_radius=2),
            mediapipe_drawing.DrawingSpec(color=(174, 139, 45),
                                   thickness=2,
                                   circle_radius=2),
        )

        if saveVideo:
            out.write(frame)
        cv2.imshow('Video', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    capture.release()
    if saveVideo:
        out.release()
    cv2.destroyAllWindows()