import cv2 
import numpy as np

cap=cv2.VideoCapture('drift.jpg')

while True:
    
    _, frame= cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # Mostraer color plantas
    plantas_bajo = np.array([10,0,0])
    plantas_alto = np.array([255,255,180])
    
    mask_plantas = cv2.inRange(hsv, plantas_bajo, plantas_alto)
    res_plantas = cv2.bitwise_and(frame, frame, mask=mask_plantas)

    # Mostrar color coche rojo
    cr_bajo = np.array([80,80,0])
    cr_alto = np.array([255,255,255])

    mask_cr = cv2.inRange(hsv, cr_bajo, cr_alto)
    res_cr = cv2.bitwise_and(frame, frame, mask=mask_cr)

    # Mostrar color coches
    coches_bajo = np.array([50,30,0])
    coches_alto = np.array([255,255,255])

    mask_coches = cv2.inRange(hsv, coches_bajo, coches_alto)
    res_coches = cv2.bitwise_and(frame, frame, mask=mask_coches)
    
    # Mostrar ventanas
    cv2.imshow("Drift", frame)

    # cv2.imshow("Mascara plantas", mask_plantas)
    cv2.imshow("Resultado plantas", res_plantas)

    # cv2.imshow("Mascara cr", mask_cr)
    cv2.imshow("Resultado coche rojo", res_cr)

    # cv2.imshow("Mascara coches", mask_coches)
    cv2.imshow("Resultado coches", res_coches)
    
    
    
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
    
cv2.destroyAllWindows()
cap.release()
