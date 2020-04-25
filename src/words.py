import cv2 as cv
import numpy as np
#
img = cv.imread('./allimg/5747.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = np.array(img)
img = img[170:2483,15:1281]
img = cv.resize(img, (2084,3807), interpolation = cv.INTER_AREA)


img = np.array(img)

height, width = img.shape[:2]
white_streak = 0
tl = (0, 0)
bl = (0, 0)
print(height/47)
count = 1
for i in range(1, height, 81):
    tl = (0, i)

    for j in range(0, width):
        arr = img[i:i + 75, j]

        if all(z > 200 for z in arr):
            white_streak = white_streak + 1

        else:
            if white_streak >= 10:
                if tl[0] != j - white_streak and tl[0]-j+white_streak <0:

                    cv.rectangle(img, tl, (j - white_streak, i + 79), (0, 255, 0))
                    crp_img = img[tl[1]: i + 79, tl[0]: j - white_streak]
                    cv.imwrite('./test/{}.jpg'.format(count),crp_img)
                    count = count + 1

                tl = (j, i)
                white_streak = 0
            else:
                white_streak = 0
    cv.rectangle(img, tl, (j - white_streak, i + 79), (0, 255, 0))
    crp_img = img[tl[1]: i + 79, tl[0]: j - white_streak]
    cv.imwrite('./test/{}.jpg'.format(count), crp_img)
    count = count + 1
print(count)
cv.imwrite('suc.png', img)
