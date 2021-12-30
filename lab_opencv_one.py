import cv2
import mediapipe as mp
import time
# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     cv2.imshow("image", img)
#     cv2.waitKey(1)
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)

#-------------------------------------------

# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils

# while True:
#     success, img = cap.read()
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = hands.process(imgRGB)
#     print(results.multi_hand_landmarks)

#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
#     cv2.imshow("image", img)
#     cv2.waitKey(1)
#     cv2.destroyAllWindows()

#-------------------------------------------

# cap = cv2.VideoCapture(0)

# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils
# num = 0
# four = 0
# eight = 0
# while True:
#     success, img = cap.read()
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = hands.process(imgRGB)
#     # print(results.multi_hand_landmarks)
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             for id , lm in enumerate(handLms.landmark):
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w) , int(lm.y * w)
#                 print(id, cx, cy)
#                 if (int(id) == 4):
#                     four = cx
#                 elif (int(id) == 5):
#                     five = cx
#                 elif (int(id) == 8):
#                     eight = cx
#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
#     cv2.putText(img, str(num), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255 , 0 ,255) , 3)
#     if(four >= eight) or (four >= five):
#         num = 5
#     else:
#         num = 4
#     cv2.imshow("image", img)
#     cv2.waitKey(1)


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
arax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    num = 5
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
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    if(arax[4] < arax[8]) or (arax[4] < arax[5]) or (aray[3] < aray[4]) or (arax[4] < arax[3]):
        num -= 1
    if((aray[8] > aray[7]) and (aray[7] > aray[6])):
        num -= 1
    if((aray[12] > aray[11]) and (aray[11] > aray[10])):
        num -= 1
    if((aray[16] > aray[15]) and (aray[15] > aray[14])):
        num -= 1
    if((aray[20] > aray[19]) and (aray[19] > aray[18]) ):
        num -= 1

    cv2.putText(img, str(num), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255 , 0 ,255) , 3)
    cv2.imshow("image", img)
    cv2.waitKey(1)
