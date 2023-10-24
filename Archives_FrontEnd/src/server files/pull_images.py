import sqlite3
import base64
import json
def db_pull():
    # Connect to the database
    conn = sqlite3.connect(r'C:\\Users\\isede\\VA_Archives_Project\\python files\\SQL  files\\archive_in_SQL.db')
    cursor = conn.cursor()

    # Fetch all shelves
    # cursor.execute("SELECT * FROM Shelves")
    # shelves = cursor.fetchall()
    # for shelf in shelves:
    #     print(shelf)

    # Fetch all boxes for a specific shelf
    # shelf_id = 'some_uuid'  # Replace this with a valid UUID from your Shelves table
    # cursor.execute("SELECT * FROM Boxes")
    # boxes = cursor.fetchall()
    # for box in boxes:
    #     print(box)

    # Fetch all image_records for a specific box
    name = 'Box 1'  # Replace this with a valid UUID from your Boxes table
    cursor.execute("SELECT id,image_data FROM Images WHERE box_id IN (SELECT id FROM Boxes WHERE name = ?)", (name,))
    image_records = cursor.fetchall()
    if image_records:
        images = []
        for record in image_records:
            try:
                image_id, image_data= record
                image_object= {
                    'id': image_id,
                    'photo_data': base64.b64encode(image_data).decode('utf-8')
                },
                images.append(image_object)
                # with open(f'output{i}.jpg','wb') as f:
                #     print(type(image_records), type(image), i)
                #     f.write(image[0])
                # i+=1
            except Exception as e:
                print(f'Error: {e}')
    # print(images)

    # Close the cursor and the connection
    cursor.close()
    conn.close()
    return images
