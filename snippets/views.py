from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, permissions, viewsets, renderers
from django.contrib.auth.models import User as Admin
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action

from snippets.models import Snippet, Users
from snippets.serializers import SnippetSerializer, UsersSerializer, AdminSerializer
from snippets.permissions import IsOwnerOrReadOnly


# ViewSets
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


# Snippet Classes
class AdminList(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FindAdminById(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DeletePutSnippetById(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FindSnippetById(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Snippet Methods
class Snippets(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               generics.GenericAPIView, ):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# User Classes
class GetCreateUser(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


# User Methods
class User(APIView):

    @api_view(['DELETE'])
    def deleteById(self, id):
        return UsersSerializer.deleteById(id)

    @api_view(['PUT'])
    def change(self, id):
        return UsersSerializer.change(self, id)

    @api_view(['GET'])
    def findById(self, id):
        return UsersSerializer.findById(id)
