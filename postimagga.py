import requests
import json
import shutil
import os

api_key = 'acc_fe01e1d58c18775'
api_secret = '29c9a1af4521b845d6d9b7d3ec55a6b5'
image_dir = 'imagenes/'

CLASSIFICATION_PATH = 'clasificacion/'
CATEGORIES = ['car', 'ship', 'bicycle']
FILE_SEP = os.sep

def checkPaths(categories, classification_path):
    if not os.path.exists(classification_path):
        os.mkdir(classification_path)
    for category in categories:
        target_path = os.path.join(classification_path, category)
        try:
            os.mkdir(target_path)
        except FileExistsError:
            print(f"El directorio '{target_path}' ya existe.")
        else:
            print(f"Se creó el directorio '{target_path}'.")


def classifyImage(image_paths, categories, classification_path):
    print(image_paths)
    classifications = {}

    # Crea el directorio principal si no existe
    os.makedirs(classification_path, exist_ok=True)

    for image_path in image_paths:
        response = requests.get(image_path)
        if response.status_code == 200:
            # Obtener el nombre de archivo de la URL
            filename = os.path.basename(image_path)

            data = requests.post(
                'https://api.imagga.com/v2/tags',
                auth=(api_key, api_secret),
                files={'image': response.content}
            ).json()

            assigned_category = None
            for tag in data['result']['tags']:
                for category in categories:
                    if tag['confidence'] == 100 and tag['tag']['en'] == category:
                        assigned_category = category
                        break

            if assigned_category:
                # Crea el directorio de la categoría si no existe
                category_path = os.path.join(classification_path, assigned_category)
                os.makedirs(category_path, exist_ok=True)

                # Ruta completa del archivo guardado
                file_path = os.path.join(category_path, filename)

                # Guardar la imagen en el directorio de la categoría
                with open(file_path, 'wb') as f:
                    f.write(response.content)

                classifications[image_path] = assigned_category
            else:
                print(f"No se pudo clasificar la imagen: {image_path}")
        else:
            print(f"Error fetching image: {image_path}")

    return classifications

