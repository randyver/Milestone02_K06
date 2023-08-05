import cv2
import pickle

# size rectangle
width, height = 80, 120


# read file KotakParkir
try:
    with open('KotakParkir', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

# add end delete rectangle
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < (x1 + width) and y1 < y < (y1 + height):
                posList.pop(i)

    # update data
    with open('KotakParkir', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('image.jpg')

    # draw rectangle
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)

    # stop program
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 