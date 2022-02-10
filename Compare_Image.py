
from skimage.metrics import structural_similarity
import imutils
import cv2
#pip install scikit-image
#pip install imutils
#pip install opencv-python


def Compare_Image(image1,image2):
    imageA = cv2.imread(image1)
    imageB = cv2.imread(image2)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #getting the structural similarity between the images
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    #Threshold differences
    thresh = cv2.threshold(diff, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    for c in cnts:
        #Displaying Rectangles on image difference
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    if score==1.0:
        print("Reference and Test images are same")
        return True
    else:
        print("Reference and Test images are different")
        return False