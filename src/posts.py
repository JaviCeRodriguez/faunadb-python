# CRUD con FaunaDB

from os import name
from modules.crud import CRUD

db = CRUD("usuarios")

name_collection = 'posts'

db.create_collection(name_collection)

db.create_index_by_title(name_collection, 'posts_by_title')

db.create_index_by_tags(name_collection, 'posts_by_tags_with_title')

db.create_post(name_collection, "What I had for breakfast ..")

db.create_post_id(name_collection, "The first post", "1")

db.create_several_posts(name_collection, 
    [
    "My cat and other marvels",
    "Pondering during a commute",
    "Deep meanings in a latte"
    ]
)

print(f'Encontré por id {db.retrieve_post_id(name_collection, "1")}')

print(f'Encontré por titulo {db.retrieve_post_title("posts_by_title", "Pondering during a commute")}')

db.update_post(name_collection, "1", {"data": {"tags": ["pet", "cute"]}})
print(f'Actualizo por id {db.retrieve_post_id(name_collection, "1")}')

db.replace_post_title(name_collection, "1", "My dog and other marvels")
print(f'Reemplazo titulo por id {db.retrieve_post_id(name_collection, "1")}')

print(f'Elimino {db.delete_post_id(name_collection, "1")}')