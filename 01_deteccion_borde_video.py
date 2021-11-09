import cv2
import numpy as np
from time import sleep

# Abrir archivo de video
cap = cv2.VideoCapture('video_pr.mp4')

# Ancho y alto del video
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Code para archivo de video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Archivo de salida
# 30 --> fps
out = cv2.VideoWriter('new_video.mp4', fourcc, 30, (w,h))

# Mostrar todo el video
for i in range(150): # revisar que el video esté abierto
    ret, img = cap.read()
    # revisar que haya más frames
    if ret == False:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst, None)
    img[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('imagen', img)
    # gravación del video
    out.write(img)
    
    # Salida con tecla ESC
    if cv2.waitKey(1) == 27:
        break
    
    sleep(1/30)