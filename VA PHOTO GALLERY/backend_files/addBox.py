import sqlite3
import uuid

def addBoxToShelf(shelf_id, box):
    try:
        conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
        cursor = conn.cursor()

        # Fetch all boxes
        # cursor.execute("SELECT name FROM Boxes")
        # boxes = cursor.fetchall()

        # # Flatten the list of tuples to a list of strings
        # box_names = [box[0] for box in boxes]
        # shelf_name = 'Shelf ' + str(shelf_number)
        # box = 'Box ' + str(box)
        # print(box, shelf_name)
    
        # Check if shelf already exists
        cursor.execute('SELECT name FROM Shelves WHERE id = ?', (shelf_id,))
        shelf_result = cursor.fetchone()
        shelf_result = shelf_result[0]
        
        cursor.execute('SELECT name FROM Boxes WHERE name = ?', (box,))
        box_result = cursor.fetchone()

        if not box_result:
            box_id = str(uuid.uuid4())
            cursor.execute('INSERT INTO Boxes (id, shelf_id, name) VALUES (?, ?, ?)', (box_id, shelf_id, box))
            conn.commit()
            print(f"'{box}' added to '{shelf_result}'.")
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
