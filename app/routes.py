import os
from flask import render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from . import app

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return "Hello, this is the static delivery server"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True, 'filename': filename})
    else:
        return jsonify({'error': 'File type not allowed'})

@app.route('/uploads/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], filename
    )

if __name__ == '__main__':
    app.run(debug=True)
