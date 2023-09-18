import firebase_admin
from firebase_admin import firestore, credentials, storage


#initializing app
bucket_url = 'archives-database-e5267.appspot.com'
service_acct_key = r'C:\\Users\\isede\\VA_Archives_Project\\sdk\\service_key_archives_database_adminsdk.json'
cred = credentials.Certificate(service_acct_key)
app = firebase_admin.initialize_app(cred, {'storageBucket': bucket_url
})
# Created a Firestore client
db = firestore.client()

#created a cloud storage bucket 
bucket = storage.bucket()

#main dir name
base_directory = 'ARCHIVED IMAGES'

#shelf and the box that came from it; will be used as sub-folders for organizing 
# shelf_number = None
# box_number = None

#from image to uploadable format
def convert_to_blob(image_file, dest_path):
    blob = bucket.blob(dest_path)
    blob.upload_from_filename(image_file)
    image_url = blob.public_url
    return image_url

#sends data to firestore
def send_archive(image_url, fileName, box_number, shelf_number):
    doc_ref = db.collection("users").document(fileName)
    doc_ref.set({
        "image_url": image_url, 
        "shelf": shelf_number, 
        "box": box_number
        })

