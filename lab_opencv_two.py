import cv2
import serial
import mediapipe as mp

port = "COM4"
Serial_begin = 9600
ser = serial.Serial(port, Serial_begin)
num = "stop"
ser.write('1'.encode())
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
arax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w) , int(lm.y * h)
                arax[id] = int(cx)
                aray[id] = int(cy)
                print(cx)
                print(cy)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        if((aray[20] > aray[19]) and (aray[19] > aray[18]) ) or ((aray[16] > aray[15]) and (aray[15] > aray[14])) or ((aray[12] > aray[11]) and (aray[11] > aray[10])) or ((aray[8] > aray[7]) and (aray[7] > aray[6])):
            ser.write('1'.encode())
            num = "stop"
        else:
            if(arax[4] < arax[8]) or (arax[4] < arax[5]) or (aray[3] < aray[4]) or (arax[4] < arax[3]):
                num = "cw"
                ser.write('0'.encode())
            else:
                num = "ccw"
                ser.write('2'.encode())
    else:
        ser.write('1'.encode())
        num = "nan"
    cv2.putText(img, str(num), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255 , 0 ,255) , 3)
    cv2.imshow("image", img)

    if(cv2.waitKey(1)!=-1):
        break
print('END')
ser.write('1'.encode())
cv2.destroyAllWindows()