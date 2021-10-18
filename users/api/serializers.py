from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    # override del método create para Encriptar nuestra contraseña
    def create(self, validated_data):
        # recuperar la contraseña encriptarla  setearla en el usuario y guardarla
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) # seteando la contraseña encriptada
        instance.save()
        return instance

    # para ese un poco extraño pero la encriptación no la hacemos nosotros la hace django por nosotros

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name'] # con el serializador estamos indicando que el usuario va poder actualizar solo estos 2 datos