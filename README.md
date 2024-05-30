# AppDockerizadaNube
 Aplicación de Clasificacion de imagenes Dockerizada

 Pasos para la dockerización de la app.
 1. Primero, se debe asegurar de tener instalado Docker en la maquina.
 2. El proyecto de la aplicación con Flask, tiene un archivo llamado Dockerfile, este archivo permite crear la imagen Docker de la aplicación.


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

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/57b5fd31-375d-43a4-91b0-6b3918b607e5)


COMO USAR LA APLICACIÓN:

Una vez que la aplicación sea ejecutada en localhost:5000, vamos a ver una pantalla como la siguiente:

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/1021210c-5df3-4dfb-a681-a0b535ecf91b)

Las imágenes que se muestran, se han obtenido a partir de urls públicas. Para determinar la clasificación de las mismas, se han ocupado las siguientes categorías 'car', 'ship' y 'bicycle'. Hay que recalcar que la aplicación, tiene un directorio llamado 'clasificacion', este directorio inicialmente, se va a encontrar vacio.

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/04c1d08e-0103-46c1-9d12-18226dfb38f1)

En la pantalla hay un botón que dice analizar, simplemente debemos hacer click en este botón, y la aplicación nos va a mostrar la clasificación de las imágenes que hemos seleccionado.

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/c3504552-46fc-46b3-aaaa-3654294da090)

Como se observa, las imágenes han sido clasificadas, en las categorías que se han definido anteriormente. Además, la aplicación obtiene las imágenes de la url y las descarga. Una vez que las descarga, las clasifica en diferentes directorios dentro de 'clasificacion', dependiendo de la categoría a la que corresponde cada imagen, como se ve a continuación:

![image](https://github.com/cmdy28/AppDockerizadaNube/assets/85966698/fbf87808-9a12-4bbb-9e39-d7cfa6aa9401)






