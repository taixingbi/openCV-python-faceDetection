import cv2

# Load the cascade
cascPath= 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascPath)      

# Read the input image
img = cv2.imread('test.jpeg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces


faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces

for (x, y, w, h) in faces[:1]:
    print(x,y,w,h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


# Display the output
cv2.imshow('img', img)

cv2.waitKey()

