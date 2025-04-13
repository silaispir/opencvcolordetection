import cv2
import numpy as np

# Renk aralığını seçmek için trackbar fonksiyonları
def nothing(x):
    pass

# Pencere oluştur
cv2.namedWindow("Trackbars")

# Trackbar'lar için başlangıç değerlerini ayarla
cv2.createTrackbar("Lower-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Upper-H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("Upper-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper-V", "Trackbars", 255, 255, nothing)

# Video yakalama (webcam'den giriş için 0'ı seçin)
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()
    if not ret:
        break

    # HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'lardan değerleri al
    l_h = cv2.getTrackbarPos("Lower-H", "Trackbars")
    l_s = cv2.getTrackbarPos("Lower-S", "Trackbars")
    l_v = cv2.getTrackbarPos("Lower-V", "Trackbars")
    u_h = cv2.getTrackbarPos("Upper-H", "Trackbars")
    u_s = cv2.getTrackbarPos("Upper-S", "Trackbars")
    u_v = cv2.getTrackbarPos("Upper-V", "Trackbars")

    # Alt ve üst sınırları belirle
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    # Maske oluştur
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Orijinal görüntü üzerinde maske uygulanmış görüntü
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri göster
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()

