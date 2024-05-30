from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

# Importa las funciones de tu código corregido
from postimagga import checkPaths, classifyImage, CATEGORIES, CLASSIFICATION_PATH, image_dir

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = image_dir
image_urls = [
    'https://i.pinimg.com/236x/fd/e2/d8/fde2d833487f921bbe7dae56d7283eea.jpg',
    'https://i.pinimg.com/236x/fd/33/87/fd33870762f6f94fd800935752af0d16.jpg',
    'https://i.pinimg.com/236x/20/e2/cd/20e2cda116286ec86e75a36a5a079613.jpg',
    'https://i.pinimg.com/236x/de/bb/8e/debb8eb8c90fdfff8f63078077d0d430.jpg',
    'https://i.pinimg.com/474x/89/04/41/8904419e8970baa8a77efa72ef9a51c6.jpg'
]

# @app.route('/')
# def index():
#     images = os.listdir(image_dir)
#     return render_template('index.html', images=images)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener las URLs de las 5 imágenes
        image_paths = image_urls

        # Clasificar las imágenes
        checkPaths(CATEGORIES, CLASSIFICATION_PATH)
        classifications = classifyImage(image_paths, CATEGORIES, CLASSIFICATION_PATH)

        return render_template('classify.html', classifications=classifications)

    return render_template('index.html', image_urls=image_urls)


@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    file = request.files['image']
    if file.filename == '':
        return 'No image selected', 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    checkPaths(CATEGORIES, CLASSIFICATION_PATH)
    # classifyImage(file_path, CATEGORIES, CLASSIFICATION_PATH)
    assigned_category = classifyImage(file_path, CATEGORIES, CLASSIFICATION_PATH)
    return render_template('classify.html', category=assigned_category)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')