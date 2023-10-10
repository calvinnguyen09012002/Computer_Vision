#Đọc Ảnh, Hiển Thị Và Lưu Ảnh OpenCV Python
import cv2 
import os

path = r'C:\Visual Studio Code\Computer_Vision\Bai2\line.jpg'
path_1 = r'C:\Visual Studio Code\Computer_Vision\Bai2'

img = cv2.imread(path)

cv2.imshow('Image', img)

os.chdir(path_1)

fileName = 'New_Image.jpg'
cv2.imwrite(fileName, img)
print('thanh cong')

cv2.waitKey(0) 
cv2.destroyAllWindows()
