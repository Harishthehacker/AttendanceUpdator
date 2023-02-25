import cv2 as cv
import os


new_width = 640
new_height = 480


dpi = 300


folder_path = 'C:/Users/Harish/OneDrive/Desktop/Sample'
blur_folder_path= 'C:/Users/Harish/OneDrive/Desktop/Sample/Blur'


for filename in os.listdir(folder_path):
    
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.imec'):
        
        img = cv.imread(os.path.join(folder_path, filename))
 
        resized_img = cv.resize(img, (new_width, new_height))
        
        blur= cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
        
        cv.imwrite(os.path.join(folder_path, filename), resized_img)

        cv.imwrite(os.path.join(blur_folder_path, filename), blur)

for filename in os.listdir(blur_folder_path):
    
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.imec'):
        
        img1 = cv.imread(os.path.join(blur_folder_path, filename))
        
        resized_img1 = cv.resize(img1, (new_width, new_height))
        
        cv.imwrite(os.path.join(blur_folder_path, filename), img1)


for filename in os.listdir(blur_folder_path):

    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.imec'):
        
        img2 = cv.imread(os.path.join(blur_folder_path, filename))
        
        blur_bw= cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        cv.imwrite(os.path.join(blur_folder_path, filename), blur_bw)



        