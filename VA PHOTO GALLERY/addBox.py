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

def addBoxToShelf(shelf_number, box_number):
    try:
        conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
        cursor = conn.cursor()

        # Fetch all boxes
        # cursor.execute("SELECT name FROM Boxes")
        # boxes = cursor.fetchall()

        # # Flatten the list of tuples to a list of strings
        # box_names = [box[0] for box in boxes]
        shelf_name = 'Shelf ' + str(shelf_number)
        box = 'Box ' + str(box_number)
        print(box, shelf_name)
    
        # Check if shelf already exists
        cursor.execute('SELECT name, id FROM Shelves WHERE name = ?', (shelf_name,))
        shelf_result = cursor.fetchone()
        # shelf_result = shelf_result[0]
        # return shelf_result

        if not shelf_result:
            shelf_id = str(uuid.uuid4())
            cursor.execute('INSERT INTO Shelves (id, name) VALUES (?, ?)', (shelf_id, shelf_name))
            conn.commit()
            print(f"'{shelf_name}' with id '{shelf_id}' created and added to DB")
        else:
            cursor.execute('SELECT id FROM Shelves WHERE name = ?', (shelf_name,))
            shelf_result = cursor.fetchone()
            shelf_id = shelf_result[0]
            print('shelf in DB already')

        cursor.execute('SELECT name FROM Boxes WHERE name = ?', (box,))
        box_result = cursor.fetchone()

        if not box_result:
            box_id = str(uuid.uuid4())
            cursor.execute('INSERT INTO Boxes (id, shelf_id, name) VALUES (?, ?, ?)', (box_id, shelf_id, box))
            conn.commit()
            print(f"'{box}' added to '{shelf_name}'.")
            return True
        else:
            return (False,f"'{box}' already exists in DB")
    except sqlite3.Error as e:
        print(f'Database error: {e}')
        return False
    finally:
        cursor.close()
        conn.close()


print(addBoxToShelf(4,0))
