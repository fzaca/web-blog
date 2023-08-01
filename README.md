# Web homebanking con Flask

## Instalación

Para instalar y ejecutar esta aplicación, siga los siguientes pasos:

1. Clone este repositorio en su máquina local.
2. Cree un entorno virtual de Python utilizando virtualenv o venv y active el entorno virtual.
3. Instale los requerimientos de la aplicación utilizando el archivo `requirements.txt`:
```
$ pip install -r requirements.txt
```
4. Renombre el archivo .env.example a .env y actualice las credenciales de la base de datos.
5. Abra la terminal y ejecute los siguientes comandos para crear la base de datos:
```
flask db init
flask db migrate
flask db upgrade
```

## Ejecución

Para ejecutar la aplicación, asegúrese de haber activado su entorno virtual de Python y ejecute el siguiente comando en la terminal:
```
$ flask run
```
Una vez que la aplicación esté en ejecución, abra un navegador web y vaya a la dirección `http://localhost:5000` para acceder a la aplicación.

## Tecnologías utilizadas

* Python
* Flask
* MySQL

## Autor ✒️

**Jose Zacarías Flores**  - [Xukay101](https://github.com/Xukay101)