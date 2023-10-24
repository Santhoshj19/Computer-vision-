import cv2
import numpy as np

image = cv2.imread('your_image.jpg')

original_points = np.float32([[0, 0], [image.shape[1], 0], [0, image.shape[0], [image.shape[1], image.shape[0]]])
desired_points = np.float32([[0, 0], [300, 0], [0, 400], [300, 400]])  # Adjust the points as needed

perspective_matrix = cv2.getPerspectiveTransform(original_points, desired_points)

transformed_image = cv2.warpPerspective(image, perspective_matrix, (300, 400))  # Specify the output image size


cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



