'''
Basic for OPENCV module for loading and processing image
'''

import cv2    # importing opencv

img = cv2.imread("galaxy.jpg",0)  # Loading Image - Second Paramter is for dimensions (0 - black/white, 1 - RGB, -1 - For Transparency)

print(img.shape)    # Getting Total rows and columns
print(type(img))    # Type of Image here is NUMPY ARRAY
print(img.ndim)     # Dimensions for Image

resized_image = cv2.resize(img,(img.shape[1]//3,img.shape[0]//3))  # Resizing image

cv2.imshow("Galaxy",resized_image)  # Showing Output of the Image with the Window Name :- Here - Galaxy

cv2.imwrite("Galaxy_resized.jpg",resized_image) # Saving the Resized Image as a copy 

cv2.waitKey(0)  # Wait for key press for window close (0 - For key press else in milliseconds (ms))
cv2.destroyAllWindows() # Closing all windows


'''
For multiple images in the folder use <glob> module

EXAMPLE:-

import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)

'''
