import cv2
import numpy as np


# ##################
# ### FUNCTIONS ###
# ################

def draw_circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img,(x,y),100,(255,0,0),10)

################################
## SHOWING IMAGE WITH OPENCV ##
##############################
cv2.namedWindow(winname='dog_backpack')

cv2.setMouseCallback('dog_backpack',draw_circle)

img = cv2.imread('../Data/dog_backpack.jpg')

while True:
    cv2.imshow('dog_backpack',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()