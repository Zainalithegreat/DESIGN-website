from flask import Flask, render_template, request
import os
import uuid
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file.filename == '':
            return 'Please select an image.'
        if file and allowed_file(file.filename):
            # Generate a unique file name
            unique_filename = str(uuid.uuid4()) + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
            file_path = os.path.join('C:\Users\zaina\Desktop\DESIGN website\loginandsignup\Uploads', unique_filename)
            
            # Save the uploaded file
            file.save(file_path)
            return 'Image uploaded successfully.'
        return 'Only JPEG files are allowed.'
    else:
        return render_template('image_upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'jpeg', 'jpg'}

if __name__ == '__main__':
    app.run()

