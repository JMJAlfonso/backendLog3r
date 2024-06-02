from mongoDB import db
from bson import ObjectId


def get_imagenes_repository(user_id):
    collection = db['imagenes']
    result = collection.find(
        {
            "userId": ObjectId(user_id)
        }
    )
    imagenes = list(result)
    for imagen in imagenes:
        imagen['_id'] = str(imagen['_id'])
        imagen['userId'] = str(imagen['userId'])

    return imagenes


def post_imagenes_repository(embedding, user_id):

    collection = db['imagenes']
    result = collection.insert_one({
        "embedding": embedding,
        "userId": ObjectId(user_id)
    })

    result = {
        "_id": str(result.inserted_id),
        "embedding": embedding,
        "userId": user_id
    }

    return result
