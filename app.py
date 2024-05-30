from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

# Importa las funciones de tu código corregido
from postimagga import checkPaths, classifyImage, CATEGORIES, CLASSIFICATION_PATH, image_dir

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = image_dir
image_urls = [
    'https://i.pinimg.com/236x/a0/b2/2d/a0b22d988c49953d08df3d226ef27c8b.jpg',
    'https://i.pinimg.com/236x/6b/af/60/6baf6076bf2202e5bd1c0b86b36016b8.jpg',
    'https://i.pinimg.com/236x/47/63/a1/4763a185bb41b50f10468abea03534cb.jpg',
    'https://i.pinimg.com/236x/8f/af/fb/8faffbc8dea295806ccbe9f99ce2fbb2.jpg',
    'https://i.pinimg.com/236x/e7/cf/4c/e7cf4cf3638e79677a825d8ec5b27283.jpg',
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
        checkPaths(CLASSIFICATION_PATH)
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

    checkPaths(CLASSIFICATION_PATH)
    # classifyImage(file_path, CATEGORIES, CLASSIFICATION_PATH)
    assigned_category = classifyImage(file_path, CATEGORIES, CLASSIFICATION_PATH)
    return render_template('classify.html', category=assigned_category)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')