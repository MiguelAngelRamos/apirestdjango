from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User

#endpoints
class RegisterView(APIView):
    def post(self, request):
        # request.data son los datos nuevos que vienen del usuario
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated] # solo los usuarios autenticados podrán hacer uso este UserView para obtener los datos del usuario
    # override del método get
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    # override del método put
    def put(self, request):
        # request.user.id
        user = User.objects.get(id=request.user.id) # me devuelve la id del usuario que esta realizando la peticion
        serializer = UserUpdateSerializer(user, request.data) # user = los datos actuales del usuario, request.data los nuevos datos del usuario
        if serializer.is_valid(raise_exception=True): # si el serializer es valido cumple con los datos que se le piden pasa a caso contrario genera una exception
            serializer.save() # guardamos los nuevos datos
            return Response(serializer.data) # retornamos los nuevos datos del usuario
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)