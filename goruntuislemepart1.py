import cv2
import numpy as np

# Trackbar'lar için callback fonksiyonu (değer değiştiğinde çağrılır)
def nothing(x):
    pass

# Görüntüyü yükle
image = cv2.imread("C:/Users/silai/Desktop/image.jpg")  # 'image.jpg' yerine kendi görüntü dosyanızın adını yazın.

# Görüntüyü HSV renk uzayına dönüştür
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Yeni bir pencere oluştur
cv2.namedWindow("Mavi Renk Tespiti")

# Trackbar'ları ekle (alt ve üst HSV sınırları için)
cv2.createTrackbar("Hue Min", "Mavi Renk Tespiti", 100, 179, nothing)
cv2.createTrackbar("Hue Max", "Mavi Renk Tespiti", 140, 179, nothing)
cv2.createTrackbar("Saturation Min", "Mavi Renk Tespiti", 150, 255, nothing)
cv2.createTrackbar("Saturation Max", "Mavi Renk Tespiti", 255, 255, nothing)
cv2.createTrackbar("Value Min", "Mavi Renk Tespiti", 50, 255, nothing)
cv2.createTrackbar("Value Max", "Mavi Renk Tespiti", 255, 255, nothing)

while True:
    # Trackbar değerlerini al
    h_min = cv2.getTrackbarPos("Hue Min", "Mavi Renk Tespiti")
    h_max = cv2.getTrackbarPos("Hue Max", "Mavi Renk Tespiti")
    s_min = cv2.getTrackbarPos("Saturation Min", "Mavi Renk Tespiti")
    s_max = cv2.getTrackbarPos("Saturation Max", "Mavi Renk Tespiti")
    v_min = cv2.getTrackbarPos("Value Min", "Mavi Renk Tespiti")
    v_max = cv2.getTrackbarPos("Value Max", "Mavi Renk Tespiti")
    
    # HSV sınırlarını ayarla
    lower_blue = np.array([h_min, s_min, v_min])
    upper_blue = np.array([h_max, s_max, v_max])

    # Mavi renkleri maskelemek için bir maske oluştur
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Orijinal görüntüde sadece mavi renkleri göstermek için maskeyi uygula
    blue_detected = cv2.bitwise_and(image, image, mask=mask)

    # Görüntüleri göster
    cv2.imshow("Orijinal Görüntü", image)
    cv2.imshow("Mavi Renk Tespiti", blue_detected)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tüm pencereleri kapat
cv2.destroyAllWindows()

