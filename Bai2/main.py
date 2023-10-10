#Thao Tác Với Ảnh Số - Đọc , Hiển Thị, Lưu Ảnh trong OpenCV và Python
import cv2 

path = r'C:\LaptrinhC\Computer_Vision\Bai2\line.jpg'

img = cv2.imread(path)

cv2.imshow('Cuaso1', img)

cv2.waitKey(0) 
cv2.destroyAllWindows()
