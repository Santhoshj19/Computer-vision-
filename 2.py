import cv2


image = cv2.imread('image.jpg')


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, threshold1, threshold2)


cv2.imshow('Canny Outline', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
