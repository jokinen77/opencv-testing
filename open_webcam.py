import cv2

CAP_DEFAULT_CONTRAST = 50
CAP_DEFAULT_HUE = 50
CAP_DEFAULT_GAMMA = 50

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
cap.set(cv2.CAP_PROP_CONTRAST, CAP_DEFAULT_CONTRAST)
cap.set(cv2.CAP_PROP_HUE, CAP_DEFAULT_HUE)
cap.set(cv2.CAP_PROP_GAMMA , CAP_DEFAULT_GAMMA)

windowName = "Video"
cv2.namedWindow(windowName, cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar("Contrast", windowName, CAP_DEFAULT_CONTRAST, 100, lambda x: cap.set(cv2.CAP_PROP_CONTRAST, x))
cv2.createTrackbar("HUE", windowName, CAP_DEFAULT_HUE, 100, lambda x: cap.set(cv2.CAP_PROP_HUE, x))
cv2.createTrackbar("Gamma", windowName, CAP_DEFAULT_GAMMA, 100, lambda x: cap.set(cv2.CAP_PROP_GAMMA, x))

while cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) >= 1:
    success, img = cap.read()
    cv2.imshow(windowName, img)
    cv2.waitKey(10)

cap.release()
cv2.destroyAllWindows()
