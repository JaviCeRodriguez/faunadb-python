# Modulo que contiene métodos CRUD

import os
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from dotenv import load_dotenv

class CRUD():
    def __init__(self, name_db):
        # Cargo .env, guardo secret key e instancio el cliente
        load_dotenv()
        SECRET_ADMIN_KEY = os.getenv("ADMIN_KEY")
        self.adminClient = FaunaClient(secret=SECRET_ADMIN_KEY)

        # Creo DB
        try:
            create_db = self.adminClient.query(q.create_database({"name": name_db}))
            print(create_db)
        except:
            print(f'La base de datos {name_db} ya fue creada')

        # Creo server key para la DB creada
        if not os.getenv("SERVER_KEY"):
            create_server_key = self.adminClient.query(
            q.create_key(
                {"database": q.database(name_db), "role": "server"}
            ))
            print(create_server_key)
        else:
            print('Ya se ha creado una server key!')
            SECRET_SERVER_KEY = os.getenv("SERVER_KEY")
            self.serverClient = FaunaClient(secret=SECRET_SERVER_KEY)

    def create_collection(self, name):
        # Creo una collection
        try:
            self.serverClient.query(q.create_collection({"name": name}))
            print(f'Colleción {name} creada')
        except:
            print(f'La colección {name} ya existe')

    def create_index_by_title(self, name_collection, name_index):
        # Creo un index
        try:
            self.serverClient.query(
                q.create_index(
                    {
                    "name": name_index,
                    "source": q.collection(name_collection),
                    "terms": [{"field": ["data", "title"]}]
                    }
                ))
        except:
            print(f'El index {name_index} ya existe')

    def create_index_by_tags(self, name_collection, name_index):
        # Creo otro index
        try:
            self.serverClient.query(
                q.create_index(
                    {
                    "name": name_index,
                    "source": q.collection(name_collection),
                    "terms": [{"field": ["data", "tags"]}],
                    "values": [{"field": ["data", "title"]}]
                    }
                ))
        except:
            print(f'El index {name_index} ya existe')

    def create_post(self, name_collection, title):
        self.serverClient.query(
            q.create(
                q.collection(name_collection),
                {"data": {"title": title}}
            ))
    
    def create_post_id(self, name_collection, title, id):
        try:
            self.serverClient.query(
                q.create(
                    q.ref(q.collection(name_collection), id),
                    {"data": {"title": title}}
                ))
        except:
            print(f'El documento con id = {id} ya existe')

    def create_several_posts(self, name_collection, title_list):
        self.serverClient.query(
            q.map_(
                lambda post_title: q.create(
                q.collection(name_collection),
                {"data": {"title": post_title}}
                ), title_list
            ))

    def retrieve_post_id(self, name_collection, id):
        return self.serverClient.query(q.get(q.ref(q.collection(name_collection), id)))

    def retrieve_post_title(self, name_index, title):
        return self.serverClient.query(
            q.get(
                q.match(
                q.index(name_index),
                title
                )
            ))
    
    def update_post(self, name_collection, id, obj):
        self.serverClient.query(
            q.update(
                q.ref(q.collection(name_collection), id),
                obj
            ))

    def replace_post_title(self, name_collection, id, title):
        self.serverClient.query(
            q.replace(
                q.ref(q.collection(name_collection), id),
                {"data": {"title": title}}
            ))

    def delete_post_id(self, name_collection, id):
        return self.serverClient.query(q.delete(q.ref(q.collection(name_collection), id)))