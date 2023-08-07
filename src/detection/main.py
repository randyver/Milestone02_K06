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
    #count_occupied = 0
    for i, pos in enumerate(posList):
        x,y = pos

available_parking_spaces = [
    i for i in range(len(posList)) if cv2.countNonZero(imgPro[posList[i][1]:posList[i][1] + height, posList[i][0]:posList[i][0] + width]) <= 500]

if count_empty == 0:
    ser.write((str(count_empty) + '\n').encode('utf-8'))

if count_empty > 0:
    ser.write((str(available_parking_spaces[0] + 100) + '\n').encode('utf-8'))

ser.write((str(count_empty) + '\n').encode('utf-8'))


with open('KotakParkir', 'rb') as f:
    posList = pickle.load(f)

width, height = 80, 120

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


    cv2.imshow("Image", img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThreshold", imgThreshold)
    # cv2.imshow("ImageThres", imgMedian)

    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

# Menutup koneksi port serial saat program berakhir
ser.close()