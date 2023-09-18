import os
import base64
from configurations import *

class Archived_Image():
    pass

def grab_images():
    folder=r'images'
    image_extensions = ['.jpg', '.jpeg', '.png']

    photograph = [f for f in os.listdir(folder) 
                if os.path.isfile(os.path.join(folder, f)) and any(f.lower().endswith(ext) for ext in image_extensions)]
    #loop to grab file and information
    for fileName in photograph:
        file_path = os.path.join(folder, fileName)

        with open(file_path,'rb') as image_data:
            image_file = image_data.read()
            base64_image = base64.b64encode(image_file).decode('utf-8')
        # image_URL = convert_to_blob(file_path, f'archived_images/{fileName}')
        send_archive(base64_image, fileName, 12, 2)
            
    return f'Images found: {(len(photograph))}'


grab_images()
print('done')
 # print(f'Image Added: {fileName}')
                # # print(f'Base64 Data:\n{base64_image}')
