import cv2

cv2.namedWindow("Vista Previa")
vc = cv2.VideoCapture(0) # Dispositivo de captura que estamos utilizando

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Vista Previa", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Vista Previa")
