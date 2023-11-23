import sqlite3

def getShelves():
    conn = sqlite3.connect(r'C:\Users\isede\VA_Archives_Project\VA PHOTO GALLERY\VA_PHOTOS_ARCHIVE.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM Shelves")
    shelves = cursor.fetchall()

    return shelves


# print(getShelves())