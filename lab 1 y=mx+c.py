import cv2
import numpy as np
import random


def line(image, start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        lower, upper = min(y1, y2), max(y1, y2)
        for y in range(lower, upper + 1):
            if 0 <= x1 < image.shape[0] and 0 <= y < image.shape[1]:
                image[x1, y] = 0

    elif abs(x1 - x2) < abs(y1 - y2):
        lower, upper = min(y1, y2), max(y1, y2)
        m = (y2 - y1) / (x2 - x1)
        c = (x2 * y1 - x1 * y2) / (x2 - x1)

        for y in range(lower, upper + 1):
            x = int(round((y - c) / m))
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
                image[x, y] = 0

    else:
        lower, upper = min(x1, x2), max(x1, x2)
        m = (y2 - y1) / (x2 - x1)
        c = (x2 * y1 - x1 * y2) / (x2 - x1)

        for x in range(lower, upper + 1):
            y = int(round(m * x + c))
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
                image[x, y] = 0


img = np.ones([512, 512, 3], dtype=np.uint8) * 255

for _ in range(1000):
  P1 = (random.randint(0, 511),random.randint(0, 511))
  P2 = (random.randint(0, 511),random.randint(0, 511))
  line(img, P1, P2)

cv2.imshow('Input', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
