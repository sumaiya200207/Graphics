import cv2
import numpy as np
import random
import time

def line(image, start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= x1 < image.shape[0] and 0 <= y < image.shape[1]:
                image[x1, y] = 0
    elif abs(x1 - x2) < abs(y1 - y2):
        m = (y2 - y1) / (x2 - x1)
        c = (x2 * y1 - x1 * y2) / (x2 - x1)
        lower, upper = min(y1, y2), max(y1, y2)
        for y in range(lower, upper + 1):
            x = int(round((y - c) / m))
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
                image[x, y] = 0
    else:
        m = (y2 - y1) / (x2 - x1)
        c = (x2 * y1 - x1 * y2) / (x2 - x1)
        lower, upper = min(x1, x2), max(x1, x2)
        for x in range(lower, upper + 1):
            y = int(round(m * x + c))
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
                image[x, y] = 0

def DDA(image, start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        m = 1
    else:
        m = (y2 - y1) / (x2 - x1)

    if m < 1:
        y = y1
        for i in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= i < image.shape[0] and 0 <= int(y + m) < image.shape[1]:
                image[i][int(y + m)] = 0
            y = y + m
    if m > 1:
        x = x1
        for i in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= int(x + (1 / m)) < image.shape[0] and 0 <= i < image.shape[1]:
                image[int(x + (1 / m))][i] = 0
            x = x + (1 / m)
    if m == 1:
        for i, j in zip(range(min(x1, x2), max(x1, x2)), range(min(y1, y2), max(y1, y2))):
            if 0 <= i < image.shape[0] and 0 <= j < image.shape[1]:
                image[i][j] = 0

def BresenhamLine(image, P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    dx, dy = abs(x2 - x1), abs(y2 - y1)

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= x1 < image.shape[0] and 0 <= y < image.shape[1]:
                image[x1][y] = 0
    else:
        if dx > dy:
            I1 = 2 * (dy - dx)
            I2 = 2 * dy
            P = 2 * dy - dx
            y = y1

            for x in range(min(x1, x2), max(x1, x2) + 1):
                if P >= 0:
                    P += I1
                    y += 1
                else:
                    P += I2
                if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
                    image[x][y] = 0
        else:
            I1 = 2 * (dx - dy)
            I2 = 2 * dx
            P = 2 * dx - dy
            x = x1

            for y in range(min(y1, y2), max(y1, y2) + 1):
                if P >= 0:
                    P += I1
                    x += 1
                else:
                    P += I2
                if 0 <= x < image.shape[0] and 0 <= y < image.shape[1]:
                    image[x][y] = 0

# Create images
img_line = np.ones([700, 700, 3], dtype=np.uint8) * 255
img_dda = np.ones([700, 700, 3], dtype=np.uint8) * 255
img_bresenham = np.ones([700, 700, 3], dtype=np.uint8) * 255

# Measure execution time for Line (Original)
start_time = time.time()
for _ in range(100):
    P1 = (random.randint(0, 699), random.randint(0, 699))
    P2 = (random.randint(0, 699), random.randint(0, 699))
    line(img_line, P1, P2)
line_execution_time = time.time() - start_time
print(f"Line (Original) execution time: {line_execution_time} seconds")

# Measure execution time for DDA
start_time = time.time()
for _ in range(100):
    P1 = (random.randint(0, 699), random.randint(0, 699))
    P2 = (random.randint(0, 699), random.randint(0, 699))
    DDA(img_dda, P1, P2)
dda_execution_time = time.time() - start_time
print(f"DDA execution time: {dda_execution_time} seconds")

# Measure execution time for Bresenham
start_time = time.time()
for _ in range(100):
    P1 = (random.randint(0, 699), random.randint(0, 699))
    P2 = (random.randint(0, 699), random.randint(0, 699))
    BresenhamLine(img_bresenham, P1, P2)
bresenham_execution_time = time.time() - start_time
print(f"Bresenham execution time: {bresenham_execution_time} seconds")

# Display the output images separately
cv2.imshow('Line (Original)', img_line)
cv2.imshow('DDA', img_dda)
cv2.imshow('Bresenham', img_bresenham)

cv2.waitKey(0)
cv2.destroyAllWindows()