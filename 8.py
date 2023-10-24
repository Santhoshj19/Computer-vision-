import numpy as np
from numpy.linalg import svd


world_points = np.array([
    [X1, Y1, Z1, 1],
    [X2, Y2, Z2, 1],
  
])

image_points = np.array([
    [x1, y1],
    [x2, y2],
  
])

A = []
for i in range(len(world_points)):
    X, Y, Z, _ = world_points[i]
    x, y = image_points[i]
    A.append([-X, -Y, -Z, -1, 0, 0, 0, 0, x * X, x * Y, x * Z, x])
    A.append([0, 0, 0, 0, -X, -Y, -Z, -1, y * X, y * Y, y * Z, y])

A = np.array(A)


U, S, Vt = svd(A)
P = Vt[-1, :].reshape(3, 4)

# Now, you can decompose the projection matrix into intrinsic and extrinsic matrices if needed.

print("Projection Matrix P:")
print(P)
