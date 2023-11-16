import cv2
import mediapipe as mp
mp_drawings=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_pose=mp.solutions.pose
count=0
position=None

if __name__=='__main__':
    vedio1=cv2.VideoCapture(0)
    
    while True:
        suc,frame=vedio1.read()
        if not suc:
           break
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('vedio',frame)
        if cv2.waitKey(1) & 0XFF==27:
         break
    vedio1.release()
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
            cv2.rectangle(img,(10,260),(80,340),color=(0,0,0),thickness=2)
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
            cv2.putText(img,str(count),(30,300),cv2.FONT_HERSHEY_COMPLEX,1,color=(0,0,255),thickness=2)
            cv2.imshow('Push-up',img)
            if cv2.waitKey(1) & 0XFF==27:
             break
    cap.release()
    cv2.destroyAllWindows()
        
  

        