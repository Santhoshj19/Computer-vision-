import cv2
image = cv2.imread('your_image.jpg')


if image is not None:

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found or could not be loaded.")
