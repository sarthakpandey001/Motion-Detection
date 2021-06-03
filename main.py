import cv2

cap = cv2.VideoCapture(0) #Acessing Webcam
#Type the filepath for a file already present

ret1, frame1 = cap.read()  #Initial Frame is read
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY) #BW conversion
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0) #Smoothening Image with GaussianBlur
cv2.imshow('window', frame1)

while (True):
    ret2, frame2 = cap.read()    #Reading Subsequent Frames
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    deltaframe = cv2.absdiff(gray1, gray2)   #Comparing current Frame with Background Frames
    cv2.imshow('delta', deltaframe)
    threshold = cv2.threshold(deltaframe, 25, 255, cv2.THRESH_BINARY)[1] #Thresholding frames
    threshold = cv2.dilate(threshold, None)  #Removing all Gaps in between
    cv2.imshow('threshold', threshold)
    countour, heirarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #Countours to find white image in black Background
    for i in countour:
        if cv2.contourArea(i) < 50:
            continue

        (x, y, w, h) = cv2.boundingRect(i)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (255, 0, 0), 2)  #forming rectangle around moving objects

    cv2.imshow('window', frame2)

    if cv2.waitKey(20) == ord('q'):  #press 'q' to break out of loops and quit windows
        break
cap.release()
cv2.destroyAllWindows()