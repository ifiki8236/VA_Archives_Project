import sqlite3
import base64

def db_pull(boxID, page, page_size):
    print('entered function')
    offset = (page-1)*page_size
    # Connect to the database
    conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
    print('opened db')

    cursor = conn.cursor()

    # Fetch all image_records for a specific box
    cursor.execute("SELECT id, image_data FROM Images WHERE box_id = ? LIMIT ? OFFSET ?", (boxID,page_size,offset))

    image_records = cursor.fetchall()
    images = []

    if image_records:
        print('entered if')
        for record in image_records:
            try:
                image_id, image_data = record
                image_object = {
                    'id': image_id,
                    'photo_data': base64.b64encode(image_data).decode('utf-8')
                }
                images.append(image_object)
            except Exception as e:

                print(f'Error: {e}')
    print(f'length : {len(images)}')
    # Close the cursor and the connection
    cursor.close()
    conn.close()
    return images
