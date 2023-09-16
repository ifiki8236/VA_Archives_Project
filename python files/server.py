from flask import Flask

app = Flask(__name__)

# @app.route('/api/view_image', methods=['GET'])
# def get_image():


if __name__ == '__main__':
    app.run()