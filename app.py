from flask import Flask, render_template, redirect, request, send_from_directory # type: ignore
from werkzeug.utils import secure_filename # type: ignore
from werkzeug.exceptions import RequestEntityTooLarge # type: ignore
import os

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY']= 'uploads/'
app.config['MAX_CONTENT_LENGTH']= 16*1024*1024
app.config['ALLOWED_EXTENSIONS']= ['.jpg','.jpeg','.png','.pdf']
@app.route('/')
def index():
  files= os.listdir(app.config['UPLOAD_DIRECTORY'])
  images= []
  for file in files:
    extension = os.path.splitext(file)[1].lower()
    if extension in app.config['ALLOWED_EXTENSIONS']:
      images.append(file)
  return render_template('index.html', images= images)

@app.route('/uploads', methods= ['POST'])
def upload():
  try:
    file= request.files['file']
    extension= os.path.splitext(file.filename)[1]
    if file:
      if extension not in app.config['ALLOWED_EXTENSIONS']:
        return 'File not supported'
      file.save(os.path.join(
        app.config['UPLOAD_DIRECTORY'],
        secure_filename(file.filename)
      ))
  except RequestEntityTooLarge:
    return 'File is too LARGE'
  return redirect('/')

@app.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
    try:
        return send_from_directory(app.config['UPLOAD_DIRECTORY'], filename)
    except FileNotFoundError:
        return f"File '{filename}' not found."
