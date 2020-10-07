from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import mixins, permissions
from django.contrib.auth.models import User as Admin
from rest_framework import generics

from snippets.models import Snippet, User
from snippets.serializers import SnippetSerializer, UserSerializer, AdminSerializer
from snippets.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })


class FindAllAdmins(generics.ListAPIView):
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


class FindAllSnippets(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


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


class GetCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Users(APIView):

    @api_view(['DELETE'])
    def deleteById(self, id):
        return UserSerializer.deleteById(id)

    @api_view(['PUT'])
    def change(self, id):
        return UserSerializer.change(self, id)

    @api_view(['GET'])
    def findById(self, id):
        return UserSerializer.findById(id)
