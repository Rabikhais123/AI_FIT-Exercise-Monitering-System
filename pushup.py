import cv2
import mediapipe as mp
import numpy as np
mp_drawings=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_pose=mp.solutions.pose
pose=mp_pose.Pose()
count=0
sqcount=0
bicount=0
position=None
stage=None
def calculate_angle(a,b,c):
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    radians=np.arctan2(c[1]-b[1],c[0]-b[0])-np.arctan2(a[1]-b[1],a[0]-b[0])
    angle=np.abs(radians*180.0/np.pi)
    if angle>180.0:
        angle=360-angle
    return angle

if __name__=='__main__':
    vedio1=cv2.VideoCapture('C:\Computer_Vision\media_pipe_projevt\cover.mp4')
    
    while True:
        suc,frame1=vedio1.read()
        if not suc:
           break
        gray=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        frame1=cv2.resize(frame1,(800,600))
        cv2.imshow('AI-Fit',frame1)
      

      #PUSHUP
        if cv2.waitKey(0) & 0XFF==ord('1'):
    #if 0XFF==ord('q'):
            cap=cv2.VideoCapture('C:\Computer_Vision\media_pipe_projevt\WhatsApp Video 2023-06-03 at 12.45.07 AM (1).mp4')
            pose=mp_pose.Pose()
#with mp_pose.Pose(min_detection_confidence=0.7,min_tracking_confidence=0.7) as pose:
            while True:
                suc1,img=cap.read()
                if not suc1:
                 break
                img=cv2.cvtColor(cv2.flip(img,1),cv2.COLOR_BGR2RGB)
                result=pose.process(img) ##process duty is to identify hand in image and all values are saved to pose landmarks
                img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                img=cv2.resize(img,(600,400))
                cv2.rectangle(img,(10,260),(80,330),color=(255,255,255),thickness=-1)
                imlist=[]
                if result.pose_landmarks:   # in result variable all landmarks are identifiied , so we need to display it
                    mp_drawings.draw_landmarks(img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
                    for id,lm in enumerate(result.pose_landmarks.landmark):
                     cx=lm.x
                     cy=lm.y
                     imlist.append([id,cx,cy])
                #print(imlist)
                if len(imlist)!=0:   
                    if (imlist[12][2] and imlist[11][2]>=imlist[14][2] and imlist[13][2]):
                        position='down'
                    if (imlist[12][2] and imlist[11][2]<=imlist[14][2] and imlist[13][2]) and position=='down':
                        position='up'
                        count=count+1
                        print('COUNT',count)
                cv2.putText(img,str(count),(30,300),cv2.FONT_HERSHEY_COMPLEX,1,color=(0,0,0),thickness=3)
                cv2.imshow('Push-up',img)
                if cv2.waitKey(1) & 0XFF==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

            #SQUATS
        elif cv2.waitKey(0) & 0XFF==ord('2'):
           cap=cv2.VideoCapture('C:\Computer_Vision\media_pipe_projevt\sq.mp4')
           while True:
                suc,frame=cap.read()
                frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                result=pose.process(frame)
                frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
                landmarks=result.pose_landmarks.landmark
                cv2.rectangle(frame,(10,260),(80,330),color=(0,0,0),thickness=-1)
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
                        sqcount=sqcount+1
                cv2.putText(frame,str(sqcount),(30,300),cv2.FONT_HERSHEY_COMPLEX,1,color=(255,255,255),thickness=3)
                cv2.imshow('Squates',frame)
                if cv2.waitKey(1) & 0XFF==27:
                    break

                #BICUPS
        elif cv2.waitKey(0) & 0XFF==ord('3'):
           cap=cv2.VideoCapture('C:\Computer_Vision\media_pipe_projevt\ceps.mp4')
           while True:
                suc,frame2=cap.read()
                frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
                result=pose.process(frame2)
                frame2=cv2.cvtColor(frame2,cv2.COLOR_RGB2BGR)
                landmarks=result.pose_landmarks.landmark
                cv2.rectangle(frame2,(10,260),(80,330),color=(0,0,0),thickness=-1)
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
                        bicount=bicount+1
                cv2.putText(frame2,str(bicount),(30,300),cv2.FONT_HERSHEY_COMPLEX,1,color=(255,255,255),thickness=3)
                cv2.imshow('Bi-Ceps',frame2)
                if cv2.waitKey(1) & 0XFF==27:
                    break
                        

        elif cv2.waitKey(30) & 0XFF==27:
            break
    vedio1.release()       
    cv2.destroyAllWindows()
        
  

        