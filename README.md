# Fitness-Tracker-and-Posture-Correction
Final Project for CSE-575 Statistical Machine Learning.

# For running the project you will require the following libraries:
mediapipe (0.8.9.1 or higher)
numpy
opencv-python (4.5.5.64 or higher)
pandas

# For using a exercise video as input use:
```
python ftpc.py -t {exercise_name} -vs {file_name}
```
(Example: python ftpc.py -t pull-up -vs pull-up.mp4)

# For dynamic tracking using webcam use:
```
python ftpc.py -t {exercise_name}
```
Currently it supports the following exercises which can be used: walk, squat, push-up, pull-up, sit-up. The commands for these are given below:
```
python ftpc.py -t walk
python ftpc.py -t squat
python ftpc.py -t push-up
python ftpc.py -t pull-up
python ftpc.py -t sit-up
```

