import cv2 
import numpy as np


##################
### VARIABLES ###
################

# True while mouse button down
# False while mousebutton up
drawing = False
ix = -1
iy = -1



# ##################
# ### FUNCTIONS ###
# ################

# # def draw_circle(event,x,y,flags,param):
    
# #     if event == cv2.EVENT_LBUTTONDOWN:
# #         cv2.circle(img,(x,y),100,(0,255,0),-1)

# #     elif event == cv2.EVENT_RBUTTONDOWN:
# #         cv2.circle(img,(x,y),100,(255,0,0),-1)


def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)5

cv2.namedWindow(winname='my_drawing')

# cv2.setMouseCallback('my_drawing',draw_circle)
cv2.setMouseCallback('my_drawing',draw_rectangle)




################################
## SHOWING IMAGE WITH OPENCV ##
##############################

# img = np.zeros((512,512,3),np.int8)
# remove np.int8 for black background
img = np.zeros((512,512,3))

while True:
    cv2.imshow('my_drawing',img)

    # wait 1ms and user hitting "ESC" key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

