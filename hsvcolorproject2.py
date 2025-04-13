"""
Created on Sat Feb  1 01:31:05 2025

@author: silai
"""

import cv2
import numpy as np

# Kamerayı açmayı dene
kamera = cv2.VideoCapture(0)

# Eğer kamera açılamadıysa hata ver ve çık
if not kamera.isOpened():
    print("Kamera açılamadı.")
    exit()

# Pencere isimleri
pencere_orijinal = "Orijinal Görüntü"
pencere_maske_mavi = "Mavi Maske"
pencere_maske_yesil="Yesil Maske"
pencere_maske_kirmizi = "Kırmızı Maske"
pencere_sonuc_mavi = "Mavi Renkler"
pencere_sonuc_kirmizi = "Kırmızı Renkler"
pencere_sonuc_yesil="Yesil Renkler"

# Pencereleri oluşturuyoruz 
cv2.namedWindow(pencere_orijinal)
cv2.namedWindow(pencere_maske_mavi)
cv2.namedWindow(pencere_maske_kirmizi)
cv2.namedWindow(pencere_sonuc_mavi)
cv2.namedWindow(pencere_sonuc_kirmizi)
cv2.namedWindow(pencere_maske_yesil)
cv2.namedWindow(pencere_sonuc_yesil)


while True:
    # Kameradan bir kare al
    ret, kare = kamera.read()

    # Eğer kare alınamadıysa döngüden çık
    if not ret:
        print("Kare yakalanamadı. Bir sorun olmalı.")
        break

    # Kareyi HSV'ye çevir 
    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    # Mavi renk için HSV
    alt_mavi = np.array([100, 150, 0])
    ust_mavi = np.array([140, 255, 255])

    # Yeşil renk için HSV 
    alt_yesil = np.array([35, 40, 40])
    üst_yesil = np.array([90, 255, 255])
    
    # Kırmızı renk için HSV
    alt_kirmizi1 = np.array([0, 150, 50])
    ust_kirmizi1 = np.array([10, 255, 255])
    alt_kirmizi2 = np.array([170, 150, 50])
    ust_kirmizi2 = np.array([180, 255, 255])
    

    # Mavi rengi maskele 
    maske_mavi = cv2.inRange(hsv, alt_mavi, ust_mavi)
    
    # Yeşil maske oluştur
    maske_yesil= cv2.inRange(hsv, alt_yesil,üst_yesil)

    # Kırmızı rengi maskele 
    maske_kirmizi1 = cv2.inRange(hsv, alt_kirmizi1, ust_kirmizi1)
    maske_kirmizi2 = cv2.inRange(hsv, alt_kirmizi2, ust_kirmizi2)
    maske_kirmizi = cv2.bitwise_or(maske_kirmizi1, maske_kirmizi2)

    # Orijinal görüntüde sadece mavi olan yerleri göster
    sonuc_mavi = cv2.bitwise_and(kare, kare, mask=maske_mavi)
    
    #Orijinal görüntüde sadece yesil olan yerleri göster
    sonuc_yesil = cv2.bitwise_and(kare, kare, mask=maske_yesil)

    # Orijinal görüntüde sadece kırmızı olan yerleri göster
    sonuc_kirmizi = cv2.bitwise_and(kare, kare, mask=maske_kirmizi)

    cv2.imshow(pencere_orijinal, kare)
    cv2.imshow(pencere_maske_mavi, maske_mavi)
    cv2.imshow(pencere_maske_kirmizi, maske_kirmizi)
    cv2.imshow(pencere_sonuc_mavi, sonuc_mavi)
    cv2.imshow(pencere_sonuc_kirmizi, sonuc_kirmizi)
    cv2.imshow(pencere_maske_yesil, maske_yesil)
    cv2.imshow(pencere_sonuc_yesil, sonuc_yesil)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()