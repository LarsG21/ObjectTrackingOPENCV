import cv2


cap = cv2.VideoCapture(0)


tracker1 = cv2.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
success, img = cap.read()                       #Bild machen um Zu trackendes Objekt zu markieren.
                                                #Sollte durch ein als Datei eingelesesnes scharfes bild ersetzt werden
bbox = cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)

def drawBox(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (5, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0))


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Lost",(5,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255))


    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(5,25),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0))
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break