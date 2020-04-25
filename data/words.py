import cv2 as cv
import numpy as np

img = cv.imread('data.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = np.array(img)
height, width = img.shape[:2]
white_streak = 0
tl = (0, 0)
bl = (0, 0)

print(height, width)
for i in range(2, 3764, 82):
    tl = (0, i)

    for j in range(0, width):
        arr = img[i:i + 75, j]

        if all(z > 200 for z in arr):
            white_streak = white_streak + 1

        else:
            if white_streak >= 7:
                try:
                    if tl[0] != j-white_streak:
                        cv.rectangle(img, tl, (j - white_streak, i + 79), (0, 255, 0))

                except:
                    pass
                tl = (j, i)
                white_streak = 0
            else:
                white_streak = 0

cv.imwrite('suc.png', img)
