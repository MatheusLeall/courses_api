from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        try:
            print(request)
            user = User.objects.get(username=request.user, is_superuser=True)
        except User.DoesNotExist:
            return False
        return True