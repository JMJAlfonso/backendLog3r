import cv2
import numpy as np
import face_recognition
from mongoDB import searchMdb
import os
import time
import math
##Nivel local
ruta_script = os.path.abspath(__file__)
ruta_proyecto = os.path.dirname(os.path.dirname(ruta_script)) 
datapath = os.path.join(ruta_proyecto, 'data')   
peopleList = os.listdir(datapath)



faceClassifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
prueba_path_entrada="D:/Facultad/AAAAAAFacultad/UNGS/Ano 2024/Cuatrimestre 1/Proyecto Profesional I/TP Final/flask-backend-log3r/rostrosParaTest/esteban.jpg"
THRESHOLD=0.93
imageSize=(150,150)

vectoresLocales=[]
labels=[]




 




    
    
    
def compararConDB(image_entrada):
    
    cursor=searchMdb()
    max_user_similitude=-1
    max_similitude=0
    entrada=vectorizarImagen(image_entrada)[0]
    for user in cursor:
        
        aux=calculateCosineSimilarity(entrada,user["image"])
        print(aux)
        if(aux>max_similitude and aux>THRESHOLD):
            max_user_similitude=user
            max_similitude=aux
    
    return max_user_similitude


    



def calculateCosineSimilarity(embeddings1,embeddings2):
    dotProduct = 0.0
    norm1 = 0.0
    norm2 = 0.0
    
   
    for i in range((len(embeddings1))): 
        
        dotProduct += embeddings1[i] * embeddings2[i]
        norm1 += embeddings1[i] * embeddings1[i]
        norm2 += embeddings2[i] * embeddings2[i]
        
    
    cosine_similarity = dotProduct / (math.sqrt(norm1) * math.sqrt(norm2))
    return float(cosine_similarity)
    
     


    
def vectorizarImagen(imagen):
    
    #entrada=detectarRostro(cv2.imread(entrada))
    #entrada=cv2.imread(imagen)
    posrostro_entrada=face_recognition.face_locations(imagen)[0]
    
    
    
    vector_rostro_entrada=face_recognition.face_encodings(imagen,known_face_locations=[posrostro_entrada])
    
    
    # print(vector_rostro_entrada)
    #print(vector_rostro_prueba)
    #print(entrada[0])
    
    # cv2.rectangle(prueba,(posrostro_prueba[3],posrostro_prueba[0]),(posrostro_prueba[1],posrostro_prueba[2]),(0,255,0))
    # cv2.imshow("a",entrada)
    # cv2.waitKey(500)
    
    return vector_rostro_entrada



