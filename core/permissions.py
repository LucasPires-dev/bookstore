from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyForAuthenticatedOrFullAccessForSuperUser(BasePermission):
    def has_permission(self, request, view):
        # Se não estiver autenticado, bloqueia
        if not request.user or not request.user.is_authenticated:
            return False

        # Permite tudo para superusuário
        if request.user.is_superuser:
            return True

        # Para usuários comuns: só leitura (GET, HEAD, OPTIONS)
        return request.method in SAFE_METHODS
