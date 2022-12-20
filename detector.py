import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import legacy.connector as connector
import schedule
import mysql.connector

past_plates = []

def reset_plates():
    past_plates.clear()

def save_palte(plate,location,photo=""):
    connection = mysql.connector.connect(host='localhost',
                                    database='grad',
                                    user='root',
                                    password='Dagkiranlar')
    cursor = connection.cursor()
    query = "INSERT INTO detections (plate, photo_of_vehicle, location) VALUES (%s, %s, %s)"
    values = (plate,photo,location)
    # Execute the query
    print(cursor.execute(query, values))

    connection.commit()

    connection.close()
    cursor.close()

def find_plate(frame):

    # img = cv2.imread('images/kktc3.jpg')
    # img = cv2.imread(frame)
    img = cv2.resize(frame, (600,600))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    mask = np.zeros(gray.shape, np.uint8)
    try:
        new_image = cv2.drawContours(mask, [location], 0,255, -1)
        new_image = cv2.bitwise_and(img, img, mask=mask)
    

        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+1, y1:y2+1]

        reader = easyocr.Reader(['en'])
        result = reader.readtext(cropped_image)
        
        print(result)
        plate=result[0][-2].upper()
        if plate not in past_plates:
            print("save plate")
            save_palte(plate,"Computer Engineering department")
            past_plates.append(plate)
    except:
        pass
        


def main():
    schedule.every(5).minutes.do(reset_plates)

    cap = cv2.VideoCapture('sources/plate1.mp4')

    while(cap.isOpened()):
        schedule.run_pending()
        # Capture frame-by-frame
        ret, frame = cap.read()

        find_plate(frame)


if __name__ == "__main__":
    main()
