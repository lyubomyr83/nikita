# pip install opencv-python

import cv2

# Загрузим обученные данные
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# загрузим фото
img = cv2.imread('images/1.jpg')

# сделаем фото чёрно-белым
black_and_white_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(black_and_white_img, minNeighbors=8)
print(face_coordinates)

#        0                   1
# [[34, 18, 56, 45], [35, 77, 89, 67]]
for face in face_coordinates:

    x_lc, y_lc, x_rc, y_rc = face
    # нарисуем прямоугольник
    cv2.rectangle(img, (x_lc, y_lc), (x_lc+x_rc, y_lc+y_rc), (0, 255, 64), 3)


cv2.imshow('Face detection', img)

# основной цикл
cv2.waitKey()
