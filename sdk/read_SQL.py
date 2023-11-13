import sqlite3

# Connect to the database
conn = sqlite3.connect('../python files/SQL  files/archive_in_SQL.db')
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

# Fetch all images for a specific box
name = 'Box 1'  # Replace this with a valid UUID from your Boxes table
cursor.execute("SELECT image_data FROM Images WHERE box_id IN (SELECT id FROM Boxes WHERE name = ?)", (name,))
images = cursor.fetchall()
if images:
    for i, image in enumerate(images):
        try:
            with open(f'output{i}.jpg','wb') as f:
                print(type(images), type(image))
                f.write(image[0])
            i+=1
        except Exception as e:
            print(f'Error: {e}')


# Close the cursor and the connection
cursor.close()
conn.close()
