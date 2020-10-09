from rest_framework import serializers

from employment.models import Employment, Users


class EmploymentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employment
        fields = ('url', 'id', 'created', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('url', 'id', 'created', 'name', 'surname', 'age')
