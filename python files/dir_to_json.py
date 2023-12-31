import os
import json
import uuid

# Set the path to your archives directory
archives_path = r"E:\\Archives"
database_path = './json files/archives_in_JSON.json'
test_db = r'E:\\Test Folder'

def get_images(box_path):
    # Get a list of all files in the box_path
    # Assuming all files in the box_path are images
    images = os.listdir(box_path)
    
    # Create a dictionary to store image id and src
    image_dict = {}
    for image in images:
        # Generate a unique id for each image
        image_id = str(uuid.uuid4())
        image_dict[image_id] = {"id": image_id, "src": image}
    return image_dict

def get_boxes(shelf_path):
    # Get a list of all directories in the shelf_path
    boxes = os.listdir(shelf_path)
    
    # Create a dictionary to store box data
    box_dict = {}
    for box in boxes:
        box_path = os.path.join(shelf_path, box)
        if os.path.isdir(box_path):
            # Get images for each box and store in the dictionary
            box_dict[box] = {"images": get_images(box_path)}
    return box_dict

def get_shelves(test_db):
    # Get a list of all directories in the test_db
    shelves = os.listdir(test_db)
    
    # Create a dictionary to store shelf data
    shelf_dict = {}
    for shelf in shelves:
        shelf_path = os.path.join(test_db, shelf)
        if os.path.isdir(shelf_path):
            # Get boxes for each shelf and store in the dictionary
            shelf_dict[shelf] = get_boxes(shelf_path)
    return shelf_dict

# Generate the JSON structure
archive_data = {"archives": get_shelves(test_db)}

# Write the JSON structure to a file
with open(database_path, 'w') as json_file:
    json.dump(archive_data, json_file, indent=2)
