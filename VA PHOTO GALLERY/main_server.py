from flask import Flask, request, jsonify
from pull_images import db_pull
from pull_boxes import boxes_pull
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/store_box_data', methods=['PUT'])
def store_box_data():
    # Directly return the data back to the client
    data = request.get_json()
    app.logger.info('Data received: %s', data)
    # You might want to implement some logic here to handle the data
    return jsonify(success=True)

@app.route('/retrieve_boxes', methods=['GET'])
def get_boxes():
    data = boxes_pull()
    app.logger.info('Boxes pulled')
    return jsonify(data)

@app.route('/retrieve_images/<boxID>', methods=['GET'])
def get_images(boxID):
    # You may want to receive some identifier or parameters from request.args
    try:
        returned_images = db_pull(boxID)
        if returned_images is None:
            app.logger.warning('No images returned from db_pull')
            return jsonify({'error': 'No images returned'}), 404
        else:
            app.logger.info('Images pulled: %s', type(returned_images))
            return jsonify(returned_images)
    except Exception as e:
        app.logger.error('Error on server: %s', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500

# @app.before_request
# def before_request_logging():
#     app.logger.debug("Before request: %s %s", request.method, request.url)

# @app.after_request
# def after_request_logging(response):
#     app.logger.debug("After request: %s %s", request.method, request.url)
#     return response

if __name__ == '__main__':
    app.run(debug=True)
