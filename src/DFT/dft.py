import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20 * np.log(np.abs(fshift))

plt.imshow(magnitude, cmap='gray')
plt.title("Espectro de Frequência")
plt.axis("off")
plt.show()
