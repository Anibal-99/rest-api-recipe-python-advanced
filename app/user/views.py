"""views for the user API"""

from rest_framework import generics
from user.serializers import UserSerilizaer


class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""

    serializer_class = UserSerilizaer