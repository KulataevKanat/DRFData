from rest_framework import viewsets

from employment.models import Employment, Users
from employment.serializers import EmploymentSerializers, UserSerializer


class EmploymentViewSet(viewsets.ModelViewSet):
    queryset = Employment.objects.using('employment').all()
    serializer_class = EmploymentSerializers


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.using('employment').all()
    serializer_class = UserSerializer
