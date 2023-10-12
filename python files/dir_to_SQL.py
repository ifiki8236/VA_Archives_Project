import sqlite3
import os
import uuid
import hashlib

def calculate_img_hash(path):
    try:
        with open(path, 'rb') as f:
            data = f.read()
            hash = hashlib.sha256(data).hexdigest()
        return hash
    except Exception as error:
        print(f'Error reading {path}: {error}')
        return None

def create_and_populate_db():
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect('./SQL  files/archive_in_SQL.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Shelves (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Boxes (
        id TEXT PRIMARY KEY,
        shelf_id TEXT,
        name TEXT NOT NULL,
        FOREIGN KEY (shelf_id) REFERENCES Shelves (id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Images (
        id TEXT PRIMARY KEY,
        box_id TEXT,
        hash TEXT NOT NULL,
        src TEXT NOT NULL,
        image_data BLOB,
        FOREIGN KEY (box_id) REFERENCES Boxes (id)
    )''')

    # Set path to archives directory
    archives_path = r"E:\\Archives"
    test_db = r'E:\\Test Folder'
    i=0
    
    # Insert data into tables
    for shelf_name in os.listdir(test_db):
        shelf_path = os.path.join(test_db, shelf_name)
        if os.path.isdir(shelf_path):
            # Check if shelf already exists
            cursor.execute('SELECT id FROM Shelves WHERE name = ?', (shelf_name,))
            result = cursor.fetchone()
            if result is None:
                shelf_id = str(uuid.uuid4())
                try:
                    cursor.execute('INSERT INTO Shelves (id, name) VALUES (?, ?)', (shelf_id, shelf_name))
                except sqlite3.Error as e:
                    print(f'Database error: {e}')
            else:
                shelf_id = result[0]
            
            for box_name in os.listdir(shelf_path):
                box_path = os.path.join(shelf_path, box_name)
                if os.path.isdir(box_path):
                    # Check if box already exists
                    cursor.execute('SELECT id FROM Boxes WHERE name = ? AND shelf_id = ?', (box_name, shelf_id))
                    result = cursor.fetchone()
                    if result is None:
                        box_id = str(uuid.uuid4())
                        try:
                            cursor.execute('INSERT INTO Boxes (id, shelf_id, name) VALUES (?, ?, ?)', (box_id, shelf_id, box_name))
                        except sqlite3.Error as e:
                            print(f'Database error: {e}')
                    else:
                        box_id = result[0]
                    
                    for image_name in os.listdir(box_path):
                        image_path = os.path.join(box_path, image_name)
                        image_hash = calculate_img_hash(image_path)

                        with open(image_path, 'rb') as image_file:
                            blob_data = image_file.read()
                        # Check if image already exists
                        cursor.execute('SELECT id FROM Images WHERE hash = ?', (image_hash,))
                        result = cursor.fetchone()
                        if result is None:
                            image_id = str(uuid.uuid4())
                            try:
                                cursor.execute('INSERT INTO Images (id, box_id, hash,src, image_data) VALUES (?, ?, ?, ?, ?)', (image_id, box_id, image_hash, image_name, blob_data))
                            except sqlite3.Error as e:
                                print(f'Database error: {e}')
                        else:
                            i+=1
                            print(f'{i}: Image "{image_name}" is already in Database')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Run the function
try:
    create_and_populate_db()
    print('Done')
except Exception as e:
    print(f'An error occurred: {e}')
