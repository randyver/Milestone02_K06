



available_parking_spaces = [
    i for i in range(len(posList)) if
    cv2.countNonZero(imgPro[posList[i][1]:posList[i][1] + height, posList[i][0]:posList[i][0] + width]) <= 500
]

if count_empty == 0:
    ser.write((str(count_empty) + '\n').encode('utf-8'))

if count_empty > 0:
    ser.write((str(available_parking_spaces[0] + 100) + '\n').encode('utf-8'))

ser.write((str(count_empty) + '\n').encode('utf-8'))