from flask import Flask, request, redirect, jsonify
from flask_restful import Api, Resource, reqparse
from flask import jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

api = Api(app)


class FileUpload(Resource):
	def get(self):
		return "hello from API", 200

	def post(self):
		if 'file' not in request.files:
			resp = jsonify({'message': 'No file part in the request'})
			resp.status_code = 400
			return resp
		file = request.files['file']
		if file.filename == '':
			resp = jsonify({'message': 'No file selected for uploading'})
			resp.status_code = 400
			return resp

		filename = file.filename
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resp = jsonify({'message': 'File successfully uploaded'})
		resp.status_code = 201
		print(vars(request))
		return resp

@app.route('/api/', strict_slashes=False)
def index():
	return "Hello world! S3 and DB have been integrated !\nRegistration and Pairing Functionality has been added\n\rBrogrammers send their regards. :)"


api.add_resource(FileUpload, "/api/upload", "/api/upload/")

if __name__ == "__main__":
	app.run(debug=True)
