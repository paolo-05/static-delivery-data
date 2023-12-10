import os
import uuid
from flask import request, jsonify, send_from_directory
from . import app

def generate_unique_filename(filename):
    # Get the file extension
    _, extension = os.path.splitext(filename)

    # Generate a unique identifier using uuid
    unique_id = str(uuid.uuid4())

    # Concatenate the unique_id and extension to create a unique filename
    unique_filename = f"{unique_id}{extension}"

    return unique_filename


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
        # Generate a unique filename
        unique_filename = generate_unique_filename(file.filename)

        # Save the file with the unique filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        return jsonify({'success': True, 'filename': unique_filename})
    else:
        return jsonify({'error': 'File type not allowed'})

@app.route('/uploads/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], filename
    )

if __name__ == '__main__':
    app.run(debug=True)
