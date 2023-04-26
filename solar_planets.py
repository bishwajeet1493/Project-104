import cv2

img = cv2.imread("C:/Users/Lenovo/Downloads/Project104/PRO-104-Project-Image-main/solar-system.jpg")

cv2.putText(img, "Sun", (100,70), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0,0,150))
cv2.putText(img, "Mercury", (115,240), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (190,176), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (284,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (385,248), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (560,55), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255))
cv2.putText(img, "Saturn", (800,150), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255))
cv2.putText(img, "Uranus", (960,285), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255))
cv2.putText(img, "Neptune", (1100,150), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255))

cv2.imshow("output",img)

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)