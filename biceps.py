import cv2
import mediapipe as mp
import numpy as np
mp_drawings=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_pose=mp.solutions.pose
count=0
previous=0
stage=None
pose=mp_pose.Pose()
def calculate_angle(a,b,c):
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    radians=np.arctan2(c[1]-b[1],c[0]-b[0])-np.arctan2(a[1]-b[1],a[0]-b[0])
    angle=np.abs(radians*180.0/np.pi)
    if angle>180.0:
        angle=360-angle
    return angle
cap=cv2.VideoCapture('C:\Computer_Vision\media_pipe_projevt\ceps.mp4')
while True:
                suc,frame2=cap.read()
                frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
                result=pose.process(frame2)
                frame2=cv2.cvtColor(frame2,cv2.COLOR_RGB2BGR)
                landmarks=result.pose_landmarks.landmark
                cv2.rectangle(frame2,(10,260),(80,340),color=(0,0,0),thickness=2)
                if landmarks is not None:
                    mp_drawings.draw_landmarks(frame2,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
                    shoulder=[landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        #y=landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
                    elbow=[landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        #right_knee_y=landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y
                    wrist=[landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                    angle=calculate_angle(shoulder,elbow,wrist)

                    if angle>160:
                        stage='down'
                    if angle<120 and stage=='down':
                        stage='up'
                        count=count+1
                cv2.putText(frame2,str(count),(30,300),cv2.FONT_HERSHEY_COMPLEX,1,color=(0,0,255),thickness=2)
                cv2.imshow('Vedio',frame2)
                if cv2.waitKey(1) & 0XFF==27:
                    break
                        