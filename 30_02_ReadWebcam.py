import cv2

#read from webcame{0,1,2}
cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    #show image from webcame
    cv2.imshow('frame',frame)

    #set stop video
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
