import sqlite3
import uuid

def addBoxToShelf(boxnum, shelfdata):
    try:
        conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
        cursor = conn.cursor()

        # dataReturned = extractData(data=data)
        shelf_id = shelfdata
        box = 'Box ' + str(boxnum)

        cursor.execute('SELECT name FROM Shelves WHERE id = ?', (shelf_id,))
        shelf_result = cursor.fetchone()
        shelf_result = shelf_result[0]
        
        cursor.execute('SELECT name FROM Boxes WHERE name = ?', (box,))
        box_result = cursor.fetchone()

        print(box,shelf_id)

        if box_result:
            return (False, f"'{box}' already exists in DB")
        else:
            box_id = str(uuid.uuid4())
            cursor.execute('INSERT INTO Boxes (id, shelf_id, name) VALUES (?, ?, ?)', (box_id, shelf_id, box))
            conn.commit()
            print(f"'{box}' added to '{shelf_result}'.")
            return (True, f'{box} has been added!')
    except sqlite3.Error as e:
        print(f'Database error: {e}')
        return False
    finally:
        cursor.close()
        conn.close()

