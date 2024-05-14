from pymongo import MongoClient
import certifi

# Configuración de la conexión a MongoDB
MONGO_HOST = 'mongodb+srv://pp1-rf-user:q0cK1qe153bpS5I0@cluster.0zuctio.mongodb.net'
MONGO_PORT = 27017
MONGO_DB = 'pp1_rf'

# Crear una instancia de MongoClient
client = MongoClient(MONGO_HOST, MONGO_PORT,tlsCAFile=certifi.where())

# Obtener una referencia a la base de datos
db = client[MONGO_DB]

def searchMdb():
    # Realizar operaciones con la base de datos MongoDB
    # Por ejemplo, puedes obtener una colección y devolver algunos documentos
    collection = db['usuarios']    
    result = []
    filtro = {}
    cursor = collection.find(filtro)
    return cursor
    
    
def unionPersonaEspacios(id):
    result = db.usuarios.aggregate([
        {
        '$match': {
            '_id': id  # Filtrar por el ID de la orden deseada
        }
    },
    {
        '$lookup': {
            'from': 'roles',  # Nombre de la colección a unir
            'localField': 'rol',  # Campo de la colección "usuarios" que se relaciona con la otra colección
            'foreignField': 'nombre',  # Campo de la colección "roles" que se relaciona con la otra colección
            'as': 'roles_unidos'  # Nombre del campo donde se almacenarán los documentos de la colección unida
        }
        
    },
    {
        '$project': {
            
            'roles_unidos.lugares': 1,  # Incluir solo el campo lugares de la colección roles
            '_id': 0
            
        }
    }
])
    return result

if __name__== "__main__":
   
    searchMdb()
    