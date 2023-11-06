import sqlite3

def boxes_pull():
    # Connect to the database
    conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
    cursor = conn.cursor()

    # Fetch all boxes
    cursor.execute("SELECT id, name FROM Boxes")

    boxes = cursor.fetchall()
    # print(boxes)
    # Close the cursor and the connection
    cursor.close()
    conn.close()
    return boxes
