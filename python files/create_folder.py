import os

# Set the name of the directory to be created
path = r'/mnt/c/Users/isede/OneDrive/Desktop/Archives'

# Set the names of the folders to be created
amount=8

# Create folders with specified names in the given directory
for i in range(amount):
    i+=1
    new_folder=f'Shelf {i}'
    try:
        os.makedirs(os.path.join(path, new_folder))
        print(f"Directory '{new_folder}' created")
    except FileExistsError:
        print(f"Directory '{new_folder}' already exists")

