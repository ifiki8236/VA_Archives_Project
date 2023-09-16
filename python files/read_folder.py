import os
import base64
from configurations import *

def grab_images():
    folder=r'images'
    image_extensions = ['.jpg', '.jpeg', '.png']

    photograph = [f for f in os.listdir(folder) 
                if os.path.isfile(os.path.join(folder, f)) and any(f.lower().endswith(ext) for ext in image_extensions)]
    #loop to grab file and information
    for fileName in photograph:
        file_path = os.path.join(folder, fileName)

        with open(file_path,'rb') as image_data:
            archived_photo = image_data.read()
            base64_image = base64.b64encode(archived_photo).decode('utf-8')
            send_archive(base64_image, fileName)
            
    return f'Images found: {(len(photograph))}'


grab_images()
 # print(f'Image Added: {fileName}')
                # # print(f'Base64 Data:\n{base64_image}')
