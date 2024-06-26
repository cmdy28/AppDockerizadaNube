# AppDockerizadaNube
# Aplicación de Clasificacion de imagenes Dockerizada
Objetivo
- Realizar una práctica de consumo de un servicio entregado como SaaS.
- Explorar cómo todos los conceptos revisados hasta el momento confluyen en una solución real basada en La Nube.
- Investigar Docker y dockerizar una aplicación


# Pasos para la dockerización de la Web App
 1. Primero, se debe asegurar de tener instalado Docker en la maquina.
 2. En el proyecto, nos dirijimos al archivo postimagga.py y reemplazamos nuestra apikey y la api_secret, por las credenciales que nos proporciona imagga, al crear la cuenta.

    ![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/427e58f7-ef41-47f9-8c26-5e746e49b29b)

Una vez modificado esto, la aplicación está lista para dockersizarse.

 4. El proyecto de la aplicación con Flask, tiene un archivo llamado Dockerfile, este archivo permite crear la imagen Docker de la aplicación.


![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/76d80d0b-175c-4699-932b-7e5830a900ba)

 3. Para construir la imagen Docker de la aplicación, ejecutamos el siguiente comando:

    docker build -t mi-app-flask-imagga:latest .

 4. El parámetro -t nos permite darle un nombre a la imagen (mi-app-flask-imagga) y una versión (latest). El punto al final indica que se debe buscar el Dockerfile en el directorio actual. Si verificamos en Docker Desktop, nuestra imagen se ha creado:

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/31d33ca1-5dbb-48ad-b2b2-f7b5fb8b1766)

 5. Ahora que ya tenemos la imagen Docker contruida, podemos iniciar un contenedor con la aplicación usando el siguiente comando:

    docker run --name app-flask-imagga -p 5000:5000 mi-app-flask-imagga:latest

 6. Con esto se inicia un contenedor llamado app-flask-imagga en el puerto 5000, mismo que debería responder con la aplicación dockerizada. Si verificamos en Docker Desktop, deberíamos tener nuestro contenedor:

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/92588392-ff51-4fd5-a117-ac8a9cf9354a)

 7. Si accedemos a localhost:5000, deberíamos tener acceso a la aplicación.

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/0362039d-d816-43d7-87b8-8d3b6c509be5)



# VERIFICAR FUNCIONAMIENTO DE LA WEBAPP

Una vez que la aplicación sea ejecutada en localhost:5000, vamos a ver una pantalla como la siguiente:

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/9797bc21-0951-4fcf-8716-474420155890)


Las imágenes que se muestran, se han obtenido a partir de urls públicas. Hay que recalcar que la aplicación, tiene un directorio llamado 'clasificacion', este directorio inicialmente, se va a encontrar vacio.

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/04c1d08e-0103-46c1-9d12-18226dfb38f1)

En la pantalla hay un botón que dice analizar, simplemente debemos hacer click en este botón, y la aplicación nos va a mostrar la clasificación de las imágenes que hemos seleccionado.

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/31b330c2-c0c4-41ee-b8e6-b024db74e6d1)

Como se observa, las imágenes han sido clasificadas. Como se ha solicitado mostrar los dos resultados de mayor confianza, se muestran dos categorias. Además, la aplicación obtiene las imágenes de la url y las descarga. Una vez que las descarga, las clasifica en diferentes directorios dentro de 'clasificacion', dependiendo de la categoría a la que corresponde cada imagen, como se ve a continuación:

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/127f6f97-e255-41b4-8f41-2dfac5464e0f)


NOTA: EN CASO DE REQUERIR CAMBIARLAS IMÁGENES, PUEDE HACERLO DESDE app.py en la variable image_urls, y modificar ahí las URLs de las neuvas imágenes.




