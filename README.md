# faunadb-python
Scripts de ejemplo para el uso de FaunaDB con Python

## Instalación de venv (Windows):
1. Creamos venv: `python -m venv myenv`
2. Activamos venv: `myenv\Scripts\activate`
3. Instalamos librerías necesarias
4. Creamos archivo requirements: `pip freeze > requirements.txt`
5. Desactivamos venv: `deactivate`

## Clonando este repo (Windows):
1. Clonamos: `git clone https://github.com/JaviCeRodriguez/faunadb-python.git`
2. Repetimos pasos 1 y 2 del anterior título
3. Instalamos librerías de requirements: `pip install -r requirements.txt`

## Variables de entorno en `.env`:
```
ADMIN_KEY=key_de_db_admin
SERVER_KEY=key_de_db_server
```

## Links útiles:
- [Create, retrieve, update and delete](https://docs.fauna.com/fauna/current/tutorials/crud.html?lang=python)