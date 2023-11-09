import sqlite3
import uuid
def checkBox(box_number,shelf_name):
    # Connect to the database
    conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
    cursor = conn.cursor()

    # Fetch all boxes
    cursor.execute("SELECT name FROM Boxes")
    boxes = cursor.fetchall()

    # Flatten the list of tuples to a list of strings
    box_names = [box[0] for box in boxes]
    
    box = 'Box ' + str(box_number)
    print(box_names)
    print(box)

    # Check if the box is in the list of box names
    # addBoxToShelf(shelf_name,box_name=box,cursor=cursor)

    cursor.close()
    conn.close()

def addBoxToShelf(shelf_name, box_number):
    try:
        conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
        cursor = conn.cursor()

        # Fetch all boxes
        cursor.execute("SELECT name FROM Boxes")
        boxes = cursor.fetchall()

        # Flatten the list of tuples to a list of strings
        box_names = [box[0] for box in boxes]
        
        box = 'Box ' + str(box_number)
        print(box_names)
        print(box)
        # try to add
    
        # Check if shelf already exists
        cursor.execute('SELECT name FROM Shelves WHERE name = ?', (shelf_name,))
        shelf_result = cursor.fetchone()
        if shelf_result:
            cursor.execute('SELECT id FROM Boxes WHERE name = ? AND name = ?', (box, shelf_id))
            box_result = cursor.fetchone()
        else:
            print(f"Shelf '{shelf_name}' does not exist.")
            return False

        # Check if box already exists in this shelf
        # cursor.execute('SELECT id FROM Boxes WHERE name = ? AND name = ?', (box, shelf_id))
        # box_result = cursor.fetchone()

        if not box_result:
            box_id = str(uuid.uuid4())
            cursor.execute('INSERT INTO Boxes (id, shelf_id, name) VALUES (?, ?, ?)', (box_id, shelf_id, box))
            conn.commit()
            print(f"Box '{box}' added to shelf '{shelf_name}'.")
            return True
        else:
            print(f"Box '{box}' already exists in shelf '{shelf_name}'.")
            return False

    except sqlite3.Error as e:
        print(f'Database error: {e}')
        return False



print(checkBox(10))
