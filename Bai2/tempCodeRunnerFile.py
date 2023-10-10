import cv2
import numpy as np

image = cv2.imread("line.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canimg = cv2.Canny(gray, 50, 200)

lines = cv2.HoughLines(canimg, 1, np.pi/180, np.array([]))

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a*rho
    y0 = b*rho

    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(1))

    cv2.line(image, (x1,y1), (x2,y2), (0, 0, 255), 2)

cv2.imshow("Line detected", image)
cv2.imshow("Canny Detection", canimg)

cv2.waitKey(0)
cv2.destroyAllWindows()