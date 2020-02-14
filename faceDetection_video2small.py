import cv2
import sys

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

class faceDection:
    def __init__(self):
        print("computerVision..")
        cascPath= 'haarcascade_frontalface_default.xml'
        self.faceCascade = cv2.CascadeClassifier(cascPath)
        self.scale= 100

    def webCamera(self):
        cap = cv2.VideoCapture(0)
        return cap

    def record(self ,cap):
        frame_width = int(cap.get(3)) 
        frame_height = int(cap.get(4))
        outf= 'output/save.avi'
        out = cv2.VideoWriter(outf,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        return out

    def crop(self, img):
        dim = (self.scale, self.scale)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #print('Resized Dimensions : ',resized.shape)
        return resized

    def faceBoundingbox_(self, frame): # one image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        return faces
     
    def faceBoundingbox(self, frame): # one image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        crop_img= None
        for (x, y, w, h) in faces[:1]:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            crop_img = frame[y:y+h, x:x+w]
            crop_img= self.crop(crop_img)

        return crop_img

    def pipeline(self):
        cap= self.webCamera()
        #out= self.record(cap)

        frame_width = int(cap.get(3)) 
        frame_height = int(cap.get(4))
        outf= 'output/save.avi'
        out = cv2.VideoWriter(outf,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # crop_img= self.faceBoundingbox_(frame)
            # print(crop_img)
            # if not crop_img:
            #     out.write(crop_img)

            #     cv2.imshow('origin', frame)
            #     cv2.imshow('small', crop_img)

            faces= self.faceBoundingbox_(frame)

            #print( len(faces))
            # Draw a rectangle around the faces
            for i, (x, y, w, h) in enumerate(faces):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                crop_img = frame[y:y+h, x:x+w]
                crop_img= self.crop(crop_img)

                out.write(crop_img)

                cv2.imshow("small"+str(i), crop_img)

            cv2.imshow('origin', frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        cap.release()
        out.release()

        cv2.destroyAllWindows()

if __name__== "__main__":
    faceDection().pipeline()
