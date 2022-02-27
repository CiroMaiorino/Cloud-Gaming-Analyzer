import cv2  # Libreria lavorare con i video
import math
#############################################################
# Script per il recupero dei frame dalle registrazioni video #
#############################################################
videoName = "E:/Università/Reti/Progetto Reti Cloud/Nostro/Control/5 MB/Stadia/Control-Stadia-QualityTest-5MBLimiter.mkv"  # Dove recuperare il video

cap = cv2.VideoCapture(videoName)  # Utilizzato per l'apertura del video acquisito
frameRate = cap.get(5)  # Utilizzato per acquisire il framerate del video cv2.CAP_PROP_FPS

count = 0
while cap.isOpened():  # Finché il video non è finito
    frameNum = cap.get(1)  # Numero frame CAP_PROP_POS_FRAMES
    ret, frame = cap.read()
    if (ret != True):
        break
    if frameNum % math.floor(frameRate) == 0:
        frameName = "Resources/5MBControlStadia/frame%d.jpg" % count
        count += 1
        cv2.imwrite(frameName, frame)
cap.release()
print("Frame acquisiti")
