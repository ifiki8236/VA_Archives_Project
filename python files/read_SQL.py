import sqlite3

# Connect to the database
conn = sqlite3.connect('./SQL  files/archive_in_SQL.db')
cursor = conn.cursor()

# Fetch all shelves
cursor.execute("SELECT * FROM Shelves")
shelves = cursor.fetchall()
for shelf in shelves:
    print(shelf)

# Fetch all boxes for a specific shelf
# shelf_id = 'some_uuid'  # Replace this with a valid UUID from your Shelves table
cursor.execute("SELECT * FROM Boxes")
boxes = cursor.fetchall()
for box in boxes:
    print(box)

# Fetch all images for a specific box
# box_id = 'some_uuid'  # Replace this with a valid UUID from your Boxes table
cursor.execute("SELECT * FROM Images")
images = cursor.fetchall()
for image in images:
    print(image)

# Close the cursor and the connection
cursor.close()
conn.close()
