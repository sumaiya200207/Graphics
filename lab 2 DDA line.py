import cv2
import numpy as np


def DDA(image, start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        m = 1
    else:
        m = (y2 - y1) / (x2 - x1)

    if m < 1:
        y = y1
        for i in range(min(x1, x2), max(x1, x2)):
            image[i][int(y + m)] = 0
            y = y + m
    if m > 1:
        x = x1
        for i in range(min(y1, y2), max(y1, y2)):
            image[int(x + (1 / m))][i] = 0
            x = x + (1 / m)
    if m == 1:
        for i, j in zip(range(min(x1, x2), max(x1, x2)), range(min(y1, y2), max(y1, y2))):
            image[i][j] = 0


img1 = np.ones((512, 512, 3))


print('Enter first point : ')
X1, Y1 = map(int, input().split())
print('Enter second point : ')
X2, Y2 = map(int, input().split())

DDA(img1, (X1, Y1), (X2, Y2))


cv2.imshow('Input1', img1)


cv2.waitKey(0)
cv2.destroyAllWindows()