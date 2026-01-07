import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpeg", 0)

grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

magnitude = np.sqrt(grad_x**2 + grad_y**2)

plt.imshow(magnitude, cmap='gray')
plt.title("Mapa de Gradientes")
plt.axis("off")
plt.show()
