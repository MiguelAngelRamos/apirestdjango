from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission): # que si es admin podrá hacer todo caso contrario solo podrá leer
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True # cualquiera puede acceder a los metodos get
        else:
            return request.user.is_staff # solo los usuarios del staff podran hacer a las demas peticiones