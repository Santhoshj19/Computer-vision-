import cv2
import numpy as np

image = cv2.imread('your_image.jpg')

translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])  


transformed_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))


cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

