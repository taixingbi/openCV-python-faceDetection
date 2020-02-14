import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
frame_width = int(cap.get(3)) #Default resolutions of the frame are obtained.The default resolutions are system dependent.
frame_height = int(cap.get(4))

# frame_width = 100
# frame_height =100

outf= 'output/save.avi'
out = cv2.VideoWriter(outf,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
while(True):
  ret, frame = cap.read()
 
  if ret == True: 
     
    # Write the frame into the file 'output.avi'
    out.write(frame)
 
    # Display the resulting frame    
    cv2.imshow('frame',frame)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()
