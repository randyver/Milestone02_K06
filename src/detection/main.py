import cv2
import pickle
import cvzone
import numpy as np
import serial

# Inisialisasi port serial
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM5'
ser.open()

cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

status_list = []

def checkParkingSpace(imgPro):
    count_empty = 0
    for i, pos in enumerate(posList):
        x,y = pos

        imgCrop = imgPro[y:y+height, x:x+width]
        count = cv2.countNonZero(imgCrop)
        # cvzone.putTextRect(img, str(count), (x,y+height-10), scale=1.5, thickness=2)
    
        if count <= 500:
            color = (0, 255, 0)
            count_empty += 1
        else:
            color = (0, 0, 255)
        
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 3)

    available_parking_spaces = [
        i for i in range(len(posList)) if cv2.countNonZero(imgPro[posList[i][1]:posList[i][1] + height, posList[i][0]:posList[i][0] + width]) <= 500]

    if count_empty == 0:
        ser.write((str(count_empty) + '\n').encode('utf-8'))

    if count_empty > 0:
        ser.write((str(available_parking_spaces[0] + 100) + '\n').encode('utf-8'))

    ser.write((str(count_empty) + '\n').encode('utf-8'))


with open('src/detection/KotakParkir', 'rb') as f:
    posList = pickle.load(f)

width, height = 80, 120

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.int8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThreshold", imgThreshold)
    # cv2.imshow("ImageThres", imgMedian)

    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

# Menutup koneksi port serial saat program berakhir
ser.close()
