import cv2

image = cv2.imread('image.jpg')


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


lower_threshold = 50  
upper_threshold = 150  


edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)


cv2.imshow('Canny Outline', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
