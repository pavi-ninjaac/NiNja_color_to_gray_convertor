import cv2
import os
class Convert_image():
    count=0
    def color_gray(path,name):
        image_folder=os.path.join('static','upload')
        image_folder_2 = os.path.join(image_folder, 'gray')
        #image_name='gray'+str(Convert_image.count)+'.png'
        #print(image_name)
        image_path=os.path.join(image_folder_2,name)
        img=cv2.imread(path)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        cv2.imwrite(image_path,gray)
        Convert_image.count+=1
        return image_path
