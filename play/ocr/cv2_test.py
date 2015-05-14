#ecoding=utf-8
__author__ = 'Administrator'
import cv2
img=cv2.imread("2.jpg")

# 创建一个窗口
cv2.namedWindow("Image")
# 在窗口中显示图像
cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()