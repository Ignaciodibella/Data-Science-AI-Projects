import cv2
import time
import autopy
import numpy as np
import HandTrackingModule as htm

#Instalar:
#opencv-python
#mediapipe -> version 0.8.8.0 (otras generan errores)
#autopy -> Es necesario estar usando python3.8 como interprete (no funciona en los mas nuevos).
# https://www.youtube.com/watch?v=XqepBUU3iL0 explicación.

#Definiciones
wScr, hScr = autopy.screen.size() #Ancho y Alto de la pantalla en uso
wCam, hCam = 640, 480 #Ancho y alto ventana
frameR = 100 #Reducción de cuadro

pTime = 0

detector = htm.handDetector() #Una sola mano.
suavizante = 5 #Este parámetro permite ajustar la sensiblidad del control de mouse (a mayor valor, mas lento)
plocX, plocY = 0, 0 #ubicación previa de x e y
clocX, clocY = 0, 0 #ubicacipon actual de x e y

#Camara
cap = cv2.VideoCapture(0)

#Config proporciones ventana
cap.set(3, wCam) #Width
cap.set(4, hCam) #Height

while True:
    #Obener puntos de referencia
    #Leer Camara
    success, img = cap.read()
    img = detector.findHands(img)

    lmList, bbox = detector.findPosition(img)

    #Obtener coordenadas de la punta de los dedos índice y mayor
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:] #índice
        x2, y2 = lmList[12][1:] #Mayor

        #Verificar qué dedos están levantados
        fingers = detector.fingersUp()
        #print(fingers) # muestra una lista booleana con los dedos que estan levantados (1) y los que no(0)

        #Creo un cuadro que simula la pantalla de la computadora. Esto permite tener mas sensibilidad de movimiento en la zona inferior.
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        #Modo movimiento. Necesitamos que el índice sea el único dedo levantado.
        if fingers[1] == 1 and fingers[2] == 0: #índice levantado y mayor no

            #Convertimos las coordenadas del dedo
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            #Suavizado de movimiento:
            clocX = plocX + (x3 - plocX) / suavizante
            clocY = plocY + (y3 -plocY) / suavizante

            #Enviar coordenadas al Mouse para moverlo
            autopy.mouse.move(wScr-clocX, clocY) #wScr-x3 invierte el sentido de movimiento del mouse
            cv2.circle(img, (x1, y1), 8, (0, 149, 255), cv2.FILLED) #Muestra un punto en el índice cuando está en modo Movimiento.
            plocX, plocY = clocX, clocY #Actualizacion

        #Modo clic. Dedos índice y mayor levantados.
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, line_info = detector.findDistance(8, 12, img)
            #print(length) #Distancia entre dedos (índice y mayor)
            if length < 30: #ajustar si es necesario
                cv2.circle(img, (line_info[4], line_info[5]), 8, (0, 255, 0), cv2.FILLED)  #Muestra que se está leyendo la intención de hacer clic
                autopy.mouse.click()

#click and drag pendiente
#        if fingers[1] == 1 and fingers[0] == 1:
#            length, img, line_info = detector.findDistance(4, 8, img)
#            #print(length) #Distancia entre dedos (índice y pulgar)
#            if length < 20:
#                cv2.circle(img, (line_info[4], line_info[5]), 8, (0, 0, 255), cv2.FILLED)
#                autopy.mouse.toggle(True, 'RIGHT')

    #Frame Rate de la captura (camara)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                (255, 0, 0), 3)

    #Display Pantalla
    cv2.imshow("Image", img)
    cv2.waitKey(1)