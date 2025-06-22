import cv2
from cvzone.HandTrackingModule import HandDetector

class Boton:
    def __init__(self, posicion, ancho, alto, valor):
        self.posicion = posicion
        self.ancho = ancho
        self.alto = alto
        self.valor = valor

    def graficar(self, img):
        #img es la imagen o cuadro donde graficar el boton.
        cv2.rectangle(img, self.posicion, (self.posicion[0]+self.ancho, self.posicion[1]+self.alto),
                      (55, 55, 55), cv2.FILLED) #color y relleno.
        cv2.rectangle(img, self.posicion, (self.posicion[0] + self.ancho, self.posicion[1] + self.alto),
                      (60, 60, 60), 3) #color y grosor borde.
        cv2.putText(img, self.valor, (self.posicion[0]+34, self.posicion[1]+70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (210, 210, 210), 2) #Fuente, tamaño, color y grosor.

    def eventoClick(self, x, y): #toma el valor del "mouse" -> posición del índice.
        if self.posicion[0] < x < self.posicion[0] + self.ancho and \
                self.posicion[1] < y < self.posicion[1] + self.ancho:
            #Primero chequeo horizontalmente y despues verticalemente en qué boton estoy.
            cv2.rectangle(img, self.posicion, (self.posicion[0] + self.ancho, self.posicion[1] + self.alto),
                          (80, 80, 80), cv2.FILLED)  # color y relleno.
            cv2.rectangle(img, self.posicion, (self.posicion[0] + self.ancho, self.posicion[1] + self.alto),
                          (60, 60, 60), 3)  # color y grosor borde.
            cv2.putText(img, self.valor, (self.posicion[0] + 34, self.posicion[1] + 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (210, 210, 210), 2)  # Fuente, tamaño, color y grosor.
            return True
        else:
            return False
#Camara:
cap = cv2.VideoCapture(0) #Configurar en caso de tener mas de una cámara.
cap.set(3, 1280) #Anchura de la pantalla de video.
cap.set(4, 720)  #Altura de la pantalla de video.
detector = HandDetector(detectionCon=0.8, maxHands=1) #Si está un 80% seguro que es una mano, detectarla. #El 80% busca evitar detectar falsos clics.
                                                      #El 2do parámetro hace que detectemos una sola mano.

#Creación de botones:
listaValoresBotones = [['', '', 'D', 'C'],
                       ['7', '8', '9', '*'],
                       ['4', '5', '6', '-'],
                       ['1', '2', '3', '+'],
                       ['0', '/', '.', '=']]

listaBotones = []
for x in range(4):
    for y in range(5):
        posicion_x = x * 100 + 800
        posicion_y = y * 100 + 150
        listaBotones.append(Boton((posicion_x, posicion_y), 100, 100, listaValoresBotones[y][x]))

#definciones
ecuacion = ''
contadorDelay = 0

while True:
    #Obtener imagen de la cámara:
    success, img = cap.read()
    #Espejar imagen horizontalmente
    img = cv2.flip(img, 1) #0 = vertical / 1 = horizontal

    #Detectar Mano (una sola):
    hands, img = detector.findHands(img, flipType=False)

    #Display Pantalla Resultado y Botones "Teclado":
    #Pantalla:
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100),
                  (216, 216, 216), cv2.FILLED)  # color y relleno.
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100),
                  (60, 60, 60), 3)  # color y grosor borde.

    #Teclado:
    for boton in listaBotones:
        boton.graficar(img)

    #Chequear si hizo "clic" con la mano:
    if hands:
        lmList = hands[0]['lmList'] #puntos de los dedos. Dedo índice = 8. Dedo mayor = 12.
        length, _, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img) #Calcula la distancia entre la punta del dedo índice y la del mayor.
        #print(length) #Para calibrar distancia entre dedos que representan click
        x, y = lmList[8][:2] #tomo al dedo índice como mouse. [:2] toma solo los valores (x,y), si no pongo eso devuelve (x,y,z).
        if length < 47: #length < 47 implica que tengo los dedos juntos. Se puede ajustar a lo necesario.
            for i, boton in enumerate(listaBotones):
                if boton.eventoClick(x, y) and contadorDelay == 0:
                    valor_selec = listaValoresBotones[int(i%5)][int(i/5)] #Esto permite identificar qué boton estoy presionando.
                    if valor_selec == '=':
                        ecuacion = str(round(eval(ecuacion), 5))
                    elif valor_selec == 'D':
                        ecuacion = ecuacion[:-1]
                    elif valor_selec == 'C':
                        ecuacion = ''
                    else:
                        ecuacion += valor_selec
                    contadorDelay = 1

    #Evitar duplicados al "cliquear"
    if contadorDelay != 0:
        contadorDelay += 1
    if contadorDelay > 10:
        contadorDelay = 0

    #Mostrar Ecuacion/Resultado:
    cv2.putText(img, ecuacion, (810, 130),
                cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)  # Fuente, tamaño, color y grosor.

    #Mostrar imagen:
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    #Para limpiar display calculadora desde el teclado. --> Agregar btn a la calcu
    if key == ord('c'):
        ecuacion = ''
