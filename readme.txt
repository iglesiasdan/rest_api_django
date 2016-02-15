Consultas via http sobre una Rest Api Desarrollada usando Django 1.9.2
y a su vez utilizando el paquete djangorestframework
Dichas consultas se realizaran sobre una base de datos y el objetivo de la api es que agregue estilos sobre la busqueda que se realiza
si es tipo de ropa como shorts o franela es retornado con letra cursiva, si es un equipo como real madrid se subrayan y si es una marca la retornara en negrita.


Para la utilizacion de este proyecto existen unos pasos a seguir:
1- Crear un directorio nuevo
2- Situarse en dicho directorio creado
3- Ejecutar los comandos en este orden:
	- (virtualenv env) el cual creara un Ambiente virtual para el desarrollo en django
	- (source env/bin/activate) este comando indicara que el ambiente virtual que estara activo es el que esta situado en dicho directorio
	- (pip install django) instala en el ambiente virtual activo los archivos necesarios para iniciar un proyecto en django
	- (pip install djangorestframework) instala en el ambiente virtual activo los archivos necesarios para iniciar una rest api
	- (pip install pygments)
4- Luego de haber realizado dichos pasos procedemos a crear una nueva carpeta llamada tutorial y dentro de ella copiamos los archivos del repositorio.
5- Acceder a la carpeta que acabamos de crear y ejecutar el comando (./manage.py runserver)

Para utilizar la api debebemos escribir en el navegador web la siguiente url (http://localhost:8000/buscar/) sumandole a la url lo que se quiera buscar por ejemplo http://localhost:8000/buscar/franelas1realmadrid/ o http://localhost:8000/buscar/shorts1manchesterunited1nike/


