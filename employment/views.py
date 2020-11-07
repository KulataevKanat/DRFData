from rest_framework import viewsets

from employment.models import Employment, Users
from employment.serializers import EmploymentSerializers, UserSerializer, CreateEmploymentSerializers


class EmploymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employment.objects.using('employment').all()
    serializer_class = EmploymentSerializers


class FindEmploymentByBarcode(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'barcode'
    queryset = Employment.objects.using('employment').all()
    serializer_class = EmploymentSerializers


class CreateEmploymentViewSet(viewsets.ModelViewSet):
    queryset = Employment.objects.using('employment').all()
    serializer_class = CreateEmploymentSerializers


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.using('employment').all()
    serializer_class = UserSerializer
