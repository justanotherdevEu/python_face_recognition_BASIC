import face_recognition         #recuerda que este script sólo funciona en LINUX, habiendo instalado por consola...  pip install dlib && pip install face_recognition, a no ser que
"""algo = input("Ponme algo\t :")"""   # consigas en la cmd de Windows, pip install face_recognition (o en WSL dentro de CMD)
"""algo = algo.capitalize()
print("Algo:\t ",algo)"""
#hello
image = face_recognition.load_image_file("roma.jpeg") # let's think u got a photo, called roma.jpeg
face_locations = face_recognition.face_locations(image, model="cnn")

# fontana de Trevi
print("\n\t\t",face_locations)   #NO me interesa saber esa ubi, la sé
'''
face_recognition "/mnt/c/Users/user/Desktop/.../test_folder_photos"
'''

me = face_recognition.load_image_file("roma.jpeg")
me_encoding = face_recognition.face_encodings(me)[0]

print("\n\n\t\tme_encoding=  ",me_encoding)

#  http://www.ign.es/wcts-app/
#  https://github.com/ageitgey/face_recognition
#  https://www.coordenadas-gps.com/
#  https://dateandtime.info/es/citycoordinates.php?id=690688   buscar cómo
#      poner model para sacar el print con coordenadas en condiciones, ilegible
#  https://ourcodeworld.co/articulos/leer/841/como-instalar-y-usar-la-biblioteca-de-deteccion-y-reconocimiento-facial-de-python-en-ubuntu-1604
