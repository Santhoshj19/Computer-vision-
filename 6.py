import cv2
import numpy as np

cap = cv2.VideoCapture('your_video.mp4')


original_points = np.float32([[0, 0], [cap.get(3), 0], [0, cap.get(4)], [cap.get(3), cap.get(4)]])
desired_points = np.float32([[0, 0], [300, 0], [0, 400], [300, 400]])  # Adjust the points as needed

perspective_matrix = cv2.getPerspectiveTransform(original_points, desired_points)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (300, 400))  # Adjust the output frame size as needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        br
    transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (300, 400))

    # Write the transformed frame to the output video
    out.write(transformed_frame)

    
    cv2.imshow('Transformed Video', transformed_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()



13
