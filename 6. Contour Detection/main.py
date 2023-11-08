import cv2 as cv
import numpy as np

img = cv.imread('0. Photos\Balloon.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # chuyển ảnh xám thành ảnh grayscale

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)# làm mờ ảnh

canny = cv.Canny(blur, 125, 175) # nhị phân hóa ảnh
cv.imshow('canny', canny)

"""
contours, hierarchy = cv2.findContours(binaryImage, typeofContour, methodofContour)

contours: Danh sách các contour có trong bức ảnh nhị phân. 
        Mỗi một contour được lưu trữ dưới dạng vector các điểm

hierarchy: Danh sách các vector, chứa mối quan hệ giữa các contour.

modifiedImage: Ảnh sau khi sử dụng contour, thường chúng ta không xài đối số này

binaryImage: Ảnh nhị phân gốc. 
            Một chú ý quan trọng ở đây là sau khi sử dụng hàm findContours thì 
            giá trị của binaryImage cũng thay đổi theo, nên khi sử dụng bạn có thể 
            áp dụng binaryImage.copy() để không làm thay đổi giá trị của binaryImage

typeofContour: có các dạng sau: RETR_EXTERNAL, RETR_LIST, RETR_CCOMP, 
                                RETR_TREE, RETR_FLOODFILL.

methodofContour: Có các phương thức sau: CHAIN_APPROX_NONE, CHAIN_APPROX_SIMPLE, 
                                        CHAIN_APPROX_TC89_L1, CHAIN_APPROX_TC89_KCOS.

"""
contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(img, contours, -1, (0,255,0), 2) # vẽ lại ảnh contour vào ảnh gốc

cv.imshow('CAT', img)

cv.waitKey(0)