import os

# Set the name of the directory to be created
path = f'/mnt/c/Users/isede/OneDrive/Desktop/Archives/Shelf 1'

# Set the names of the folders to be created
boxes=[1,2,3,6,7,8,10,5]

# Create folders with specified names in the given directory
for box in boxes:
    new_folder=f'Box {box}'
    try:
        os.makedirs(os.path.join(path, new_folder))
        print(f"New Box: '{new_folder}' created")
    except FileExistsError:
        print(f"This Directory, '{new_folder}', already exists")

