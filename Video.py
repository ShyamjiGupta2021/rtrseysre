import os
import cv2

path ="Images/"

Images =[]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)

#print(len(images))
count = len(Images)
frame = cv2.imread(Images[0])
height,width,channles=frame.shape
out=cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*'DIVX'),0.8,(width,height))

for i in  range(count-1,0,-1):
    frame = cv2.imread(Images[i])
    out.write(frame)
out.release()
print("Done")
        