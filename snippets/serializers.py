from django.http import Http404
from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User as Admin
from snippets.models import Snippet, Users \
    # , LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'created', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'surname')

    @staticmethod
    def deleteById(id):
        user = Users.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def change(request, id):
        user = Users.objects.get(id=id)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def findById(id):
        try:
            user = Users.objects.get(id=id)
            serializer = UsersSerializer(user)
            return Response(serializer.data)
        except Users.DoesNotExist:
            raise Http404


class AdminSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = Admin
        fields = ('id', 'username', 'snippets')
