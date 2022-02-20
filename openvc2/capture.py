from matplotlib import image
import numpy as np
import cv2 as cv

face_select = cv.CascadeClassifier("classifier_default.xml")
image = cv.imread("globo.jpg")
image_gray = cv.cvtColor(image, cv.Color_BGR2GRAY)

faces = face_select.detecMultiScale(image_gray, 1, 3, 5)
cv.imshow("imaage", image)
cv.waitKey(0)
cv.destroyAllWindows()
