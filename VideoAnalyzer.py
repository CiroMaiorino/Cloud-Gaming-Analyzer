import cv2 #Libreria lavorare con i video
import math
#############################################################
#Script per il recupero dei frame dalle registrazioni video #
#############################################################
path = ".." #path dove salvare i frame
videoName = "nomevideo.mp4" #Dove recuperare il video

cap = cv2.VideoCapture(videoName) #Utilizzato per l'apertura del video acquisito
frameRate = cap.get(5) #Utilizzato per acquisire il framerate del video cv2.CAP_PROP_FPS

count = 0
while cap.isOpened(): #Finchè il video non è finito
    frameNum = cap.get(1)#Numero frame CAP_PROP_POS_FRAMES
    ret, frame = cap.read()
    if(ret != True):
        break
    if(frameNum % math.floor(frameRate) == 0):
        videoPath = "frame%d.jpg" %count
        count +=1
        cv2.imwrite(videoName, frame)
cap.release()
print("Frame acquisiti")