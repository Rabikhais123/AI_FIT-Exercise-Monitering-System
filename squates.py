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


cap=cv2.VideoCapture('C:\Computer_Vision\media_pipe_projevt\sq.mp4')
while True:
    suc,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=pose.process(frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    landmarks=result.pose_landmarks.landmark
    cv2.rectangle(frame,(10,260),(80,340),color=(0,0,0),thickness=2)
    if landmarks is not None:
        mp_drawings.draw_landmarks(frame,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        left_hip=[landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
        #y=landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
        left_knee=[landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
        #right_knee_y=landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y
        left_ankle=[landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
        angle=calculate_angle(left_hip,left_knee,left_ankle)

        if angle>160:
            stage='down'
        if angle<120 and stage=='down':
            stage='up'
            count=count+1

        #
    cv2.imshow('Vedio',frame)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print('Coumt',count)
