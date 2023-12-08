from flask import Flask

app = Flask(__name__, static_url_path='/uploads')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}

from app import routes
