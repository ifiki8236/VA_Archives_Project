import sqlite3
import base64
import hashlib
import uuid

def extractData(data):
    imageArray = []
    # Extract box ID (assuming it's needed for database)
    boxData = data['boxData']
    # Extract image data
    imgData = data['imageData']

    for image in imgData:
        # Decode the base64 image data
        binary_data = base64.b64decode(image['data'])
        # Create a tuple with boxData and binary image data
        imageTuple = (boxData, binary_data)
        imageArray.append(imageTuple)

    return setImages(imageArray)
def calc_img_hash(image):
    try:
        hash = hashlib.sha256(image).hexdigest()
        return hash
    except Exception as error:
        print(f'Error with image: {error}')
        return None

def makeUniqueID():
    imgID = str(uuid.uuid4())
    return imgID

def setImages(data):
    conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
    cursor = conn.cursor()
    array = []
    # Assuming there's a table named 'images' with columns 'box_id' and 'image_data'
    for tuple in data:
        boxID, imageData = tuple
        img_hash = calc_img_hash(imageData)

        cursor.execute('SELECT hash FROM Images WHERE hash = ?', (img_hash,))
        result = cursor.fetchone()

        if result:
            print("Img already exists in the database") 
        else:
            imgID = makeUniqueID()

            # print(img_hash,imgID)
            # array.append(result)
            try:
                cursor.execute('INSERT INTO Images (id, box_id, hash,src, image_data) VALUES (?, ?, ?, ?, ?)', (imgID, boxID, img_hash, img_hash, imageData))
            except Exception as e:
                print('Error: ', e)
                return None
    conn.commit()
    conn.close()

    return 'All data submitted'