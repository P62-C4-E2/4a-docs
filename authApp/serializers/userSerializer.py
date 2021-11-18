
from rest_framework       import serializers # Importacion de la libreria serializadora
from authApp.models.user  import User        #  Importacion de la clase User 

class UserSerializer(serializers.ModelSerializer): # Creamos la clase serializadora
    class Meta:
        model = User  # Usamos el modelo User 
        fields = '__all__' # Se serializan todos los campos de la clase 
