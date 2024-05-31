import requests
import json
import shutil
import os
from collections import defaultdict

api_key = 'miapikey'
api_secret = 'miapisecret'
image_dir = 'imagenes/'

CLASSIFICATION_PATH = 'clasificacion/'
CATEGORIES = ['car', 'ship', 'bicycle']
FILE_SEP = os.sep

def checkPaths(classification_path):
    if not os.path.exists(classification_path):
        os.mkdir(classification_path)


def classifyImage(image_paths, categories, classification_path):
    print(image_paths)
    classifications = defaultdict(list)

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

            # Ordenar las etiquetas por su nivel de confianza
            sorted_tags = sorted(data['result']['tags'], key=lambda x: x['confidence'], reverse=True)
            assigned_categories = []
            for tag in sorted_tags:
                category = tag['tag']['en']
                assigned_categories.append(category)
                if len(assigned_categories) == 2:
                    break

            if assigned_categories:
                for assigned_category in assigned_categories:
                    # Crea el directorio de la categoría si no existe
                    category_path = os.path.join(classification_path, assigned_category)
                    os.makedirs(category_path, exist_ok=True)

                    # Ruta completa del archivo guardado
                    file_path = os.path.join(category_path, filename)

                    # Guardar la imagen en el directorio de la categoría
                    #Guardar la imagen en el directorio de la categoría
                    with open(file_path, 'wb') as f:
                        f.write(response.content)

                print(assigned_categories)    
                classifications[image_path] = assigned_categories
            else:
                print(f"No se pudo clasificar la imagen: {image_path}")
        else:
            print(f"Error fetching image: {image_path}")

    return classifications