from flask import Flask, request, jsonify
from pull_images import db_pull
from pull_boxes import boxes_pull
from flask_cors import CORS
from pull_shelves import getShelves
from setImages import extractData
from addBox import addBoxToShelf

app = Flask(__name__)
CORS(app)

# PUT methods
@app.route('/make_box', methods=['PUT'])
def store_box_data():
    # Directly return the data back to the client
    try:
        data = request.get_json()
        app.logger.info('Data received: %s', data)
        response = addBoxToShelf(data['boxNum'],data['shelfData'])
        # print(data['boxNum'])
        # You might want to implement some logic here to handle the data
        return jsonify(response)
    except Exception as e:
        print('Error', e)
        return jsonify(success=False)
    
@app.route('/add_images', methods=['PUT'])
def put_images():
    try:
        data = request.get_json()
        img = extractData(data)
        app.logger.info('Data received: %s', img)
        # You might want to implement some logic here to handle the data
        return jsonify(success=True)
    except Exception as e:
        print('Error with images :', e)
        return jsonify(success=False), 500


# GET methods
@app.route('/retrieve_boxes', methods=['GET'])
def get_boxes():
    data = boxes_pull()
    app.logger.info('Boxes pulled')
    return jsonify(data)

@app.route('/retrieve_images/<boxID>', methods=['GET'])
def get_images(boxID):
    # You may want to receive some identifier or parameters from request.args
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('size', 10))

        # Adjust this function to support pagination
        returned_images = db_pull(boxID, page, page_size)
        if returned_images is None:
            app.logger.warning('No images returned from db_pull')
            return jsonify({'error': 'No images returned'}), 404
        else:
            app.logger.info('Images pulled: %s', type(returned_images))
            return jsonify(returned_images)
    except Exception as e:
        app.logger.error('Error on server: %s', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500
    
@app.route('/retrieve_shelves', methods=['GET'])
def get_shelves():
    try:
        data = getShelves()
        return jsonify(data)
    except Exception as e:
        app.logger.error('Error: %s', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500
    
# Start Server
if __name__ == '__main__':
    app.run(debug=True)
