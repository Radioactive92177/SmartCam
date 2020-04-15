import cv2

cap  = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('Models\haarcascade_frontalface_default.xml')
#eyes_model = cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    status , photo = cap.read()

    face_cor = face_model.detectMultiScale(photo)
    #eyes_cor = eyes_model.detectMultiScale(photo)


    if len(face_cor) == 0:
        pass
    else:
        # Drawing rectangle around the face
        face_x1 = face_cor[0][0]
        face_y1 = face_cor[0][1]

        face_x2 = face_x1 + face_cor[0][2]
        face_y2 = face_y1 + face_cor[0][3]

        # Drawing rectangle around the eyes
        """eye_x1 = eyes_cor[0][0]
        eye_y1 = eyes_cor[0][1]

        eye_x2 = eye_x1 + eyes_cor[0][2]
        eye_y2 = eye_y1 + eyes_cor[0][3]
"""
        #photo = cv2.rectangle(photo, (face_x1,face_y1), (face_x2,face_y2), [0,255,0], 2)
        #photo = cv2.rectangle(photo, (eye_x1,eye_y1), (eye_x2,eye_y2), [0,255,0], 2)

        
        cv2.putText(photo,f"No. of people :{len(face_cor)}",(0,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,51),1)
        cv2.imshow('App', photo)
        
        
        if cv2.waitKey(10) == 13:
            break
#print(f"There are {len(face_cor)} people")
cv2.destroyAllWindows()